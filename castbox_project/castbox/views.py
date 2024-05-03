from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import TemplateView, ListView, DetailView, View, FormView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Episode, Playlist, Profile
from .forms import CustomUserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.utils.decorators import method_decorator
from channel.models import Channel
from comment.models import Comment
from permissions.permissions import channel_episode_required, profile_owner_required_1, profile_owner_required_2, profile_owner_required_3, profile_owner_required_4, profile_owner_required_5, profile_owner_required_6, profile_owner_required_7, profile_owner_required_8


class SignupPageView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


class HomePageView(TemplateView):
    template_name = "home.html"


@method_decorator(profile_owner_required_1, name='dispatch')
class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = 'profiles/profile.html'
    context_object_name = 'profile'


@method_decorator(profile_owner_required_2, name='dispatch')
class ProfileChannelDetailView(LoginRequiredMixin, DetailView):
    model = Channel
    template_name = 'profiles/profile_channel_detail.html'
    context_object_name = 'channel'


@method_decorator(profile_owner_required_3, name='dispatch')
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


@method_decorator(profile_owner_required_2, name='dispatch')
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


@method_decorator(profile_owner_required_2, name='dispatch')
class ProfileChannelDeleteView(LoginRequiredMixin, DeleteView):
    model = Channel
    context_object_name = "channel"
    template_name = "profiles/profile_channel_delete.html"

    def get_success_url(self):
        profile_id = self.kwargs.get('profile_id')
        return reverse_lazy('profile', kwargs={'pk': profile_id})


@method_decorator(profile_owner_required_4, name='dispatch')
class ProfileCommentDetailView(LoginRequiredMixin, DetailView):
    model = Comment
    template_name = 'profiles/profile_comment_detail.html'
    context_object_name = 'comment'


@method_decorator(profile_owner_required_4, name='dispatch')
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


@method_decorator(profile_owner_required_4, name='dispatch')
class ProfileCommentDeleteView(LoginRequiredMixin, DeleteView):
    model = Comment
    context_object_name = "comment"
    template_name = "profiles/profile_comment_delete.html"

    def get_success_url(self):
        profile_id = self.kwargs.get('profile_id')
        return reverse_lazy('profile', kwargs={'pk': profile_id})


@method_decorator(profile_owner_required_5, name='dispatch')
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


@method_decorator(profile_owner_required_6, name='dispatch')
class ProfileEpisodeDetailView(LoginRequiredMixin, DetailView):
    model = Episode
    template_name = 'profiles/profile_episode_detail.html'
    context_object_name = 'episode'


@method_decorator(profile_owner_required_6, name='dispatch')
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


@method_decorator(profile_owner_required_6, name='dispatch')
class ProfileEpisodeDeleteView(LoginRequiredMixin, DeleteView):
    model = Episode
    context_object_name = "episode"
    template_name = "profiles/profile_episode_delete.html"

    def get_success_url(self):
        profile_id = self.kwargs.get('profile_id')
        channel_id = self.kwargs.get('channel_id')
        return reverse('profile_channel_detail', kwargs={'profile_id': profile_id, 'pk': channel_id})


@method_decorator(profile_owner_required_3, name='dispatch')
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


@method_decorator(profile_owner_required_7, name='dispatch')
class ProfilePlaylistDetailView(LoginRequiredMixin, DetailView):
    model = Playlist
    template_name = 'profiles/profile_playlist_detail.html'
    context_object_name = 'playlist'


@method_decorator(profile_owner_required_7, name='dispatch')
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


@method_decorator(profile_owner_required_7, name='dispatch')
class ProfilePlaylistDeleteView(LoginRequiredMixin, DeleteView):
    model = Playlist
    context_object_name = "playlist"
    template_name = "profiles/profile_playlist_delete.html"

    def get_success_url(self):
        profile_id = self.kwargs.get('profile_id')
        return reverse_lazy('profile', kwargs={'pk': profile_id})


@method_decorator(profile_owner_required_8, name='dispatch')
class ProfilePlaylistEpisodeDeleteView(LoginRequiredMixin, View):
    def get(self, request, profile_id, pk, episode_id):
        playlist = get_object_or_404(Playlist, id=pk)
        episode = get_object_or_404(playlist.episode, id=episode_id)
        return render(request, 'profiles/profile_playlist_episode_delete.html', {'episode': episode, 'playlist': playlist})

    def post(self, request, profile_id, pk, episode_id):
        playlist = get_object_or_404(Playlist, id=pk)
        episode = get_object_or_404(playlist.episode, id=episode_id)
        playlist.episode.remove(episode)
        return HttpResponseRedirect(reverse('profile_playlist_detail', args=[profile_id, pk]))


class SelectPlaylistForm(LoginRequiredMixin, forms.Form):
    playlist = forms.ChoiceField(choices=[])

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super(SelectPlaylistForm, self).__init__(*args, **kwargs)
        self.fields['playlist'].choices = [
            (playlist.id, playlist.title) for playlist in user.playlists.all()]


@method_decorator(channel_episode_required, name='dispatch')
class EpisodeSelectPlaylistView(LoginRequiredMixin, FormView):
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

