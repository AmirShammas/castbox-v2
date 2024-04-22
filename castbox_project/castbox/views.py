from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import TemplateView, ListView, DetailView
from .models import Channel, Episode
from .forms import CustomUserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin


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

class EpisodeListView(LoginRequiredMixin, ListView):
    model = Episode
    context_object_name = "episode_list"
    template_name = "episodes/episode_list.html"
    login_url = "login"

    def get_queryset(self):
        return Episode.objects.all()

