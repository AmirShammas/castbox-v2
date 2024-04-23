from django.urls import path
from .views import ChannelListView, CommentCreateView, EpisodeListView, SignupPageView, HomePageView

urlpatterns = [
    path("accounts/signup/", SignupPageView.as_view(), name="signup"),
    path("", HomePageView.as_view(), name="home"),
    path("channel/", ChannelListView.as_view(), name="channel_list"),
    path("channel/<int:channel_id>/episode/", EpisodeListView.as_view(), name="episode_list"),
    path("channel/<int:channel_id>/comment/", CommentCreateView.as_view(), name="comment_new"),
]
