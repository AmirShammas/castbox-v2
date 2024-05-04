from .models import Comment
from profilee.models import Profile
from channel.models import Channel
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView


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
