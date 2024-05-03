from .models import Channel
from log.models import Log
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView


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
        Log.objects.create(user=request.user,
                           message=log_message, channel=channel)
        return super().get(request, *args, **kwargs)
