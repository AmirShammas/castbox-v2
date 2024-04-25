from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Channel, CustomUser, Episode, Comment, Profile
from .forms import CustomUserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse


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


class EpisodeListView(LoginRequiredMixin, ListView):
    model = Episode
    context_object_name = "episode_list"
    template_name = "episodes/episode_list.html"
    login_url = "login"

    def get_queryset(self):
        channel_id = self.kwargs.get('channel_id')
        channel = get_object_or_404(Channel, id=channel_id)
        return Episode.objects.filter(channel=channel)

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

