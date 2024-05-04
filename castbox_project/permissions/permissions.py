from django.shortcuts import get_object_or_404
from django.http import HttpResponseForbidden
from channel.models import Channel
from episode.models import Episode
from comment.models import Comment
from playlist.models import Playlist
from profilee.models import Profile


def superuser_required(view_func):
    def decorated_view_func(request, *args, **kwargs):
        if not request.user.is_superuser:
            message = "<h1>Access Denied !! Back to <a href='/'>Home</a> page !!</h1>"
            return HttpResponseForbidden(message)
        return view_func(request, *args, **kwargs)
    return decorated_view_func


def channel_episode_required(view_func):
    def decorated_view_func(request, *args, **kwargs):
        channel = get_object_or_404(Channel, pk=kwargs['channel_id'])
        episode = get_object_or_404(Episode, pk=kwargs['pk'])
        if not episode.channel == channel:
            message = "<h1>Access Denied !! Back to <a href='/'>Home</a> page !!</h1>"
            return HttpResponseForbidden(message)
        return view_func(request, *args, **kwargs)
    return decorated_view_func


def profile_owner_required_1(view_func):
    def decorated_view_func(request, *args, **kwargs):
        profile = get_object_or_404(Profile, pk=kwargs['pk'])
        if not request.user == profile.owner:
            message = "<h1>Access Denied !! Back to <a href='/'>Home</a> page !!</h1>"
            return HttpResponseForbidden(message)
        return view_func(request, *args, **kwargs)
    return decorated_view_func


def profile_owner_required_2(view_func):
    def decorated_view_func(request, *args, **kwargs):
        profile = get_object_or_404(Profile, pk=kwargs['profile_id'])
        channel = get_object_or_404(Channel, pk=kwargs['pk'])
        if not request.user == profile.owner or not request.user == channel.owner:
            message = "<h1>Access Denied !! Back to <a href='/'>Home</a> page !!</h1>"
            return HttpResponseForbidden(message)
        return view_func(request, *args, **kwargs)
    return decorated_view_func


def profile_owner_required_3(view_func):
    def decorated_view_func(request, *args, **kwargs):
        profile = get_object_or_404(Profile, pk=kwargs['profile_id'])
        if not request.user == profile.owner:
            message = "<h1>Access Denied !! Back to <a href='/'>Home</a> page !!</h1>"
            return HttpResponseForbidden(message)
        return view_func(request, *args, **kwargs)
    return decorated_view_func


def profile_owner_required_4(view_func):
    def decorated_view_func(request, *args, **kwargs):
        profile = get_object_or_404(Profile, pk=kwargs['profile_id'])
        channel = get_object_or_404(Channel, pk=kwargs['channel_id'])
        comment = get_object_or_404(Comment, pk=kwargs['pk'])
        if not request.user == profile.owner or not comment.channel == channel or not request.user == comment.author:
            message = "<h1>Access Denied !! Back to <a href='/'>Home</a> page !!</h1>"
            return HttpResponseForbidden(message)
        return view_func(request, *args, **kwargs)
    return decorated_view_func


def profile_owner_required_5(view_func):
    def decorated_view_func(request, *args, **kwargs):
        profile = get_object_or_404(Profile, pk=kwargs['profile_id'])
        channel = get_object_or_404(Channel, pk=kwargs['channel_id'])
        if not request.user == profile.owner or not request.user == channel.owner:
            message = "<h1>Access Denied !! Back to <a href='/'>Home</a> page !!</h1>"
            return HttpResponseForbidden(message)
        return view_func(request, *args, **kwargs)
    return decorated_view_func


def profile_owner_required_6(view_func):
    def decorated_view_func(request, *args, **kwargs):
        profile = get_object_or_404(Profile, pk=kwargs['profile_id'])
        channel = get_object_or_404(Channel, pk=kwargs['channel_id'])
        episode = get_object_or_404(Episode, pk=kwargs['pk'])
        if not request.user == profile.owner or not request.user == channel.owner or not request.user == episode.owner or not episode.channel == channel:
            message = "<h1>Access Denied !! Back to <a href='/'>Home</a> page !!</h1>"
            return HttpResponseForbidden(message)
        return view_func(request, *args, **kwargs)
    return decorated_view_func


def profile_owner_required_7(view_func):
    def decorated_view_func(request, *args, **kwargs):
        profile = get_object_or_404(Profile, pk=kwargs['profile_id'])
        playlist = get_object_or_404(Playlist, pk=kwargs['pk'])
        if not request.user == profile.owner or not request.user == playlist.user:
            message = "<h1>Access Denied !! Back to <a href='/'>Home</a> page !!</h1>"
            return HttpResponseForbidden(message)
        return view_func(request, *args, **kwargs)
    return decorated_view_func


def profile_owner_required_8(view_func):
    def decorated_view_func(request, *args, **kwargs):
        profile = get_object_or_404(Profile, pk=kwargs['profile_id'])
        playlist = get_object_or_404(Playlist, pk=kwargs['pk'])
        episode = get_object_or_404(Episode, pk=kwargs['episode_id'])
        if not request.user == profile.owner or not request.user == playlist.user or not episode in playlist.episode.all():
            message = "<h1>Access Denied !! Back to <a href='/'>Home</a> page !!</h1>"
            return HttpResponseForbidden(message)
        return view_func(request, *args, **kwargs)
    return decorated_view_func
