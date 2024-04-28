from django import forms
from django.http import HttpResponseForbidden, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import TemplateView, ListView, DetailView, View, FormView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Channel, CustomUser, Episode, Comment, Follow, Like, Log, Playlist, Profile
from .forms import CustomUserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.utils.decorators import method_decorator


def superuser_required(view_func):
    def decorated_view_func(request, *args, **kwargs):
        if not request.user.is_superuser:
            message = "<h1>Access Denied !! Back to <a href='/'>Home</a> page !!</h1>"
            return HttpResponseForbidden(message)
        return view_func(request, *args, **kwargs)
    return decorated_view_func


class SignupPageView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


class HomePageView(TemplateView):
    template_name = "home.html"


class ChannelListView(LoginRequiredMixin, ListView):
    model = Channel
    context_object_name = "channel_list"
    template_name = "channels/channel_list.html"
    login_url = "login"

    def get_queryset(self):
        return Channel.objects.all()
    
class ChannelDetailView(LoginRequiredMixin, DetailView):
    model = Channel
    context_object_name = "channel"
    template_name = "channels/channel_detail.html"
    login_url = "login"

    def get(self, request, *args, **kwargs):
        channel = get_object_or_404(Channel, pk=self.kwargs['pk'])
        log_message = f"The user '{request.user}' watched the channel '{channel.title}' !!"
        Log.objects.create(user=request.user, message=log_message, channel=channel)
        return super().get(request, *args, **kwargs)


class ChannelFollowView(LoginRequiredMixin, View):
    def post(self, request, pk):
        channel = get_object_or_404(Channel, id=pk)
        user = request.user
        
        if Follow.objects.filter(user=user, channel=channel).exists():
            return HttpResponseRedirect(reverse('channel_detail', kwargs={'pk': pk}))
        
        new_follow = Follow.objects.create(user=user, channel=channel)

        profile = Profile.objects.get(owner=self.request.user)
        profile.follow.add(new_follow)
        
        return HttpResponseRedirect(reverse('channel_detail', kwargs={'pk': pk}))


class ChannelUnfollowView(LoginRequiredMixin, View):
    def post(self, request, pk):
        channel = get_object_or_404(Channel, id=pk)
        user = request.user
        
        if not Follow.objects.filter(user=user, channel=channel).exists():
            return HttpResponseRedirect(reverse('channel_detail', kwargs={'pk': pk}))
        
        follow_to_delete = Follow.objects.filter(user=user, channel=channel).first()
        if follow_to_delete:
            follow_to_delete.delete()
            profile = Profile.objects.get(owner=self.request.user)
            profile.follow.remove(follow_to_delete)
        
        return HttpResponseRedirect(reverse('channel_detail', kwargs={'pk': pk}))


class EpisodeListView(LoginRequiredMixin, ListView):
    model = Episode
    context_object_name = "episode_list"
    template_name = "episodes/episode_list.html"
    login_url = "login"

    def get_queryset(self):
        channel_id = self.kwargs.get('channel_id')
        channel = get_object_or_404(Channel, id=channel_id)
        return Episode.objects.filter(channel=channel)


class EpisodeDetailView(LoginRequiredMixin, DetailView):
    model = Episode
    template_name = 'episodes/episode_detail.html'
    context_object_name = 'episode'


class EpisodeLikeView(LoginRequiredMixin, View):
    def post(self, request, channel_id, pk):
        channel = get_object_or_404(Channel, id=channel_id)
        episode = get_object_or_404(Episode, id=pk)
        user = request.user
        
        if Like.objects.filter(user=user, channel=channel, episode=episode).exists():
            return HttpResponseRedirect(reverse('episode_detail', kwargs={'channel_id': channel_id, 'pk': pk}))
        
        new_like = Like.objects.create(user=user, channel=channel, episode=episode)

        profile = Profile.objects.get(owner=self.request.user)
        profile.like.add(new_like)
        
        return HttpResponseRedirect(reverse('episode_detail', kwargs={'channel_id': channel_id, 'pk': pk}))


class EpisodeUnlikeView(LoginRequiredMixin, View):
    def post(self, request, channel_id, pk):
        channel = get_object_or_404(Channel, id=channel_id)
        episode = get_object_or_404(Episode, id=pk)
        user = request.user
        
        if not Like.objects.filter(user=user, channel=channel, episode=episode).exists():
            return HttpResponseRedirect(reverse('episode_detail', kwargs={'channel_id': channel_id, 'pk': pk}))
        
        like_to_delete = Like.objects.filter(user=user, channel=channel, episode=episode).first()
        if like_to_delete:
            like_to_delete.delete()
            profile = Profile.objects.get(owner=self.request.user)
            profile.like.remove(like_to_delete)
        
        return HttpResponseRedirect(reverse('episode_detail', kwargs={'channel_id': channel_id, 'pk': pk}))


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    context_object_name = "comment"
    template_name = "comments/comment_new.html"
    fields = ["title", "description"]
    login_url = "login"

    def form_valid(self, form):
        form.instance.author = self.request.user
        channel_id = self.kwargs.get('channel_id')
        channel = get_object_or_404(Channel, id=channel_id)
        form.instance.channel = channel
        form.save()

        profile = Profile.objects.get(owner=self.request.user)
        profile.comment.add(form.instance)

        return super().form_valid(form)
    
    def get_success_url(self):
        channel_id = self.kwargs.get('channel_id')
        return reverse('channel_detail', kwargs={'pk': channel_id})


class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = 'profiles/profile.html'
    context_object_name = 'profile'


class ProfileChannelDetailView(LoginRequiredMixin, DetailView):
    model = Channel
    template_name = 'profiles/profile_channel_detail.html'
    context_object_name = 'channel'


class ProfileChannelCreateView(LoginRequiredMixin, CreateView):
    model = Channel
    context_object_name = "channel"
    template_name = "profiles/profile_channel_new.html"
    fields = ["title", "description"]
    login_url = "login"

    def get_success_url(self):
        profile_id = self.kwargs.get('profile_id')
        return reverse_lazy('profile', kwargs={'pk': profile_id})

    def form_valid(self, form):
        form.instance.owner = self.request.user
        form.save()

        profile = Profile.objects.get(owner=self.request.user)
        profile.channel.add(form.instance)

        return super().form_valid(form)

class ProfileChannelUpdateView(LoginRequiredMixin, UpdateView):
    model = Channel
    context_object_name = "channel"
    template_name = "profiles/profile_channel_edit.html"
    fields = ["title", "description"]
    login_url = "login"

    def get_success_url(self):
        profile_id = self.kwargs.get('profile_id')
        return reverse_lazy('profile', kwargs={'pk': profile_id})

    def form_valid(self, form):
        form.instance.owner = self.request.user
        form.save()

        return super().form_valid(form)


class ProfileChannelDeleteView(LoginRequiredMixin, DeleteView):
    model = Channel
    context_object_name = "channel"
    template_name = "profiles/profile_channel_delete.html"
    
    def get_success_url(self):
        profile_id = self.kwargs.get('profile_id')
        return reverse_lazy('profile', kwargs={'pk': profile_id})


class ProfileCommentDetailView(LoginRequiredMixin, DetailView):
    model = Comment
    template_name = 'profiles/profile_comment_detail.html'
    context_object_name = 'comment'


class ProfileCommentUpdateView(LoginRequiredMixin, UpdateView):
    model = Comment
    context_object_name = "comment"
    template_name = "profiles/profile_comment_edit.html"
    fields = ["title", "description"]
    login_url = "login"

    def get_success_url(self):
        profile_id = self.kwargs.get('profile_id')
        return reverse_lazy('profile', kwargs={'pk': profile_id})

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.save()

        return super().form_valid(form)


class ProfileCommentDeleteView(LoginRequiredMixin, DeleteView):
    model = Comment
    context_object_name = "comment"
    template_name = "profiles/profile_comment_delete.html"
    
    def get_success_url(self):
        profile_id = self.kwargs.get('profile_id')
        return reverse_lazy('profile', kwargs={'pk': profile_id})


class ProfileEpisodeCreateView(LoginRequiredMixin, CreateView):
    model = Episode
    context_object_name = "episode"
    template_name = "profiles/profile_episode_new.html"
    fields = ["title", "description"]
    login_url = "login"

    def form_valid(self, form):
        form.instance.owner = self.request.user
        channel_id = self.kwargs.get('channel_id')
        channel = get_object_or_404(Channel, id=channel_id)
        form.instance.channel = channel
        form.save()

        profile = Profile.objects.get(owner=self.request.user)
        profile.episode.add(form.instance)

        return super().form_valid(form)
    
    def get_success_url(self):
        profile_id = self.kwargs.get('profile_id')
        channel_id = self.kwargs.get('channel_id')
        return reverse('profile_channel_detail', kwargs={'profile_id': profile_id, 'pk': channel_id})


class ProfileEpisodeDetailView(LoginRequiredMixin, DetailView):
    model = Episode
    template_name = 'profiles/profile_episode_detail.html'
    context_object_name = 'episode'


class ProfileEpisodeUpdateView(LoginRequiredMixin, UpdateView):
    model = Episode
    context_object_name = "episode"
    template_name = "profiles/profile_episode_edit.html"
    fields = ["title", "description"]
    login_url = "login"
    
    def get_success_url(self):
        profile_id = self.kwargs.get('profile_id')
        channel_id = self.kwargs.get('channel_id')
        episode_id = self.kwargs.get('pk')
        return reverse_lazy('profile_episode_detail', kwargs={'profile_id': profile_id, 'channel_id': channel_id, 'pk': episode_id})
    
    def form_valid(self, form):
        form.instance.owner = self.request.user
        form.save()
        return super().form_valid(form)


class ProfileEpisodeDeleteView(LoginRequiredMixin, DeleteView):
    model = Episode
    context_object_name = "episode"
    template_name = "profiles/profile_episode_delete.html"
    
    def get_success_url(self):
        profile_id = self.kwargs.get('profile_id')
        channel_id = self.kwargs.get('channel_id')
        return reverse('profile_channel_detail', kwargs={'profile_id': profile_id, 'pk': channel_id})


class ProfilePlaylistCreateView(LoginRequiredMixin, CreateView):
    model = Playlist
    context_object_name = "playlist"
    template_name = "profiles/profile_playlist_new.html"
    fields = ["title"]
    login_url = "login"

    def get_success_url(self):
        profile_id = self.kwargs.get('profile_id')
        return reverse_lazy('profile', kwargs={'pk': profile_id})

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()

        profile = Profile.objects.get(owner=self.request.user)
        profile.playlist.add(form.instance)

        return super().form_valid(form)


class ProfilePlaylistDetailView(LoginRequiredMixin, DetailView):
    model = Playlist
    template_name = 'profiles/profile_playlist_detail.html'
    context_object_name = 'playlist'


class ProfilePlaylistUpdateView(LoginRequiredMixin, UpdateView):
    model = Playlist
    context_object_name = "playlist"
    template_name = "profiles/profile_playlist_edit.html"
    fields = ["title"]
    login_url = "login"

    def get_success_url(self):
        profile_id = self.kwargs.get('profile_id')
        return reverse_lazy('profile', kwargs={'pk': profile_id})

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()

        return super().form_valid(form)


class ProfilePlaylistDeleteView(LoginRequiredMixin, DeleteView):
    model = Playlist
    context_object_name = "playlist"
    template_name = "profiles/profile_playlist_delete.html"
    
    def get_success_url(self):
        profile_id = self.kwargs.get('profile_id')
        return reverse_lazy('profile', kwargs={'pk': profile_id})


class ProfilePlaylistEpisodeDeleteView(View):
    def get(self, request, profile_id, pk, episode_id):
        playlist = get_object_or_404(Playlist, id=pk)
        episode = get_object_or_404(playlist.episode, id=episode_id)
        return render(request, 'profiles/profile_playlist_episode_delete.html', {'episode': episode, 'playlist': playlist})

    def post(self, request, profile_id, pk, episode_id):
        playlist = get_object_or_404(Playlist, id=pk)
        episode = get_object_or_404(playlist.episode, id=episode_id)
        playlist.episode.remove(episode)
        return HttpResponseRedirect(reverse('profile_playlist_detail', args=[profile_id, pk]))


class SelectPlaylistForm(forms.Form):
    playlist = forms.ChoiceField(choices=[])

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super(SelectPlaylistForm, self).__init__(*args, **kwargs)
        self.fields['playlist'].choices = [(playlist.id, playlist.title) for playlist in user.playlists.all()]


class EpisodeSelectPlaylistView(FormView):
    template_name = 'episodes/episode_select_playlist.html'
    form_class = SelectPlaylistForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        playlist_id = form.cleaned_data['playlist']
        episode_id = self.kwargs['pk']
        playlist = Playlist.objects.get(pk=playlist_id)
        episode = Episode.objects.get(pk=episode_id)

        if episode in playlist.episode.all():
            return HttpResponseRedirect(reverse('episode_detail', kwargs={'channel_id': self.kwargs['channel_id'], 'pk': self.kwargs['pk']}))

        playlist.episode.add(episode)

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('episode_detail', kwargs={'channel_id': self.kwargs['channel_id'], 'pk': self.kwargs['pk']})


class EpisodePlayView(LoginRequiredMixin, DetailView):
    model = Episode
    template_name = 'episodes/episode_play.html'
    context_object_name = 'episode'

    def get(self, request, *args, **kwargs):
        episode = get_object_or_404(Episode, pk=self.kwargs['pk'])
        log_message = f"The user '{request.user}' played the episode '{episode.title}' !!"
        Log.objects.create(user=request.user, message=log_message, channel=episode.channel, episode=episode)
        return super().get(request, *args, **kwargs)


@method_decorator(superuser_required, name='dispatch')
class LogListView(LoginRequiredMixin, ListView):
    model = Log
    context_object_name = "log_list"
    template_name = "logs/log_list.html"
    login_url = "login"

    def get_queryset(self):
        return Log.objects.all()

