from channel.models import Channel
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Episode
from django.views.generic import ListView, DetailView
from django.utils.decorators import method_decorator
from permissions.permissions import channel_episode_required
from castbox.models import Log


class EpisodeListView(LoginRequiredMixin, ListView):
    model = Episode
    context_object_name = "episode_list"
    template_name = "episodes/episode_list.html"
    login_url = "login"

    def get_queryset(self):
        channel_id = self.kwargs.get('channel_id')
        channel = get_object_or_404(Channel, id=channel_id)
        return Episode.objects.filter(channel=channel)


@method_decorator(channel_episode_required, name='dispatch')
class EpisodeDetailView(LoginRequiredMixin, DetailView):
    model = Episode
    template_name = 'episodes/episode_detail.html'
    context_object_name = 'episode'


@method_decorator(channel_episode_required, name='dispatch')
class EpisodePlayView(LoginRequiredMixin, DetailView):
    model = Episode
    template_name = 'episodes/episode_play.html'
    context_object_name = 'episode'

    def get(self, request, *args, **kwargs):
        episode = get_object_or_404(Episode, pk=self.kwargs['pk'])
        log_message = f"The user '{request.user}' played the episode '{episode.title}' !!"
        Log.objects.create(user=request.user, message=log_message,
                           channel=episode.channel, episode=episode)
        return super().get(request, *args, **kwargs)
