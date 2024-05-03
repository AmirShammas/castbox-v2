from channel.models import Channel
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Episode
from django.utils.decorators import method_decorator
from permissions.permissions import channel_episode_required
from .models import Like
from django.views.generic import View
from django.urls import reverse
from django.http import HttpResponseRedirect
from castbox.models import Profile


@method_decorator(channel_episode_required, name='dispatch')
class EpisodeLikeView(LoginRequiredMixin, View):
    def post(self, request, channel_id, pk):
        channel = get_object_or_404(Channel, id=channel_id)
        episode = get_object_or_404(Episode, id=pk)
        user = request.user

        if Like.objects.filter(user=user, channel=channel, episode=episode).exists():
            return HttpResponseRedirect(reverse('episode_detail', kwargs={'channel_id': channel_id, 'pk': pk}))

        new_like = Like.objects.create(
            user=user, channel=channel, episode=episode)

        profile = Profile.objects.get(owner=self.request.user)
        profile.like.add(new_like)

        return HttpResponseRedirect(reverse('episode_detail', kwargs={'channel_id': channel_id, 'pk': pk}))


@method_decorator(channel_episode_required, name='dispatch')
class EpisodeUnlikeView(LoginRequiredMixin, View):
    def post(self, request, channel_id, pk):
        channel = get_object_or_404(Channel, id=channel_id)
        episode = get_object_or_404(Episode, id=pk)
        user = request.user

        if not Like.objects.filter(user=user, channel=channel, episode=episode).exists():
            return HttpResponseRedirect(reverse('episode_detail', kwargs={'channel_id': channel_id, 'pk': pk}))

        like_to_delete = Like.objects.filter(
            user=user, channel=channel, episode=episode).first()
        if like_to_delete:
            like_to_delete.delete()
            profile = Profile.objects.get(owner=self.request.user)
            profile.like.remove(like_to_delete)

        return HttpResponseRedirect(reverse('episode_detail', kwargs={'channel_id': channel_id, 'pk': pk}))
