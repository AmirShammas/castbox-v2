from django.urls import path
from .views import ChannelListView, EpisodeListView, SignupPageView, HomePageView

urlpatterns = [
    path("accounts/signup/", SignupPageView.as_view(), name="signup"),
    path("", HomePageView.as_view(), name="home"),
    path("channel/", ChannelListView.as_view(), name="channel_list"),
    path("episode/", EpisodeListView.as_view(), name="episode_list"),
]
