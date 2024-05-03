from .models import Follow
from castbox.models import Profile
from channel.models import Channel
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.views.generic import View


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

        follow_to_delete = Follow.objects.filter(
            user=user, channel=channel).first()
        if follow_to_delete:
            follow_to_delete.delete()
            profile = Profile.objects.get(owner=self.request.user)
            profile.follow.remove(follow_to_delete)

        return HttpResponseRedirect(reverse('channel_detail', kwargs={'pk': pk}))
