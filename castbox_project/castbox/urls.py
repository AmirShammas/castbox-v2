from django.urls import path
from .views import ChannelCreateView, ChannelListView, CommentCreateView, EpisodeListView, ProfileDetailView, SignupPageView, HomePageView

urlpatterns = [
    path("accounts/signup/", SignupPageView.as_view(), name="signup"),
    path("", HomePageView.as_view(), name="home"),
    path("channel/", ChannelListView.as_view(), name="channel_list"),
    path("channel/<int:channel_id>/episode/", EpisodeListView.as_view(), name="episode_list"),
    path("channel/<int:channel_id>/comment/", CommentCreateView.as_view(), name="comment_new"),
    path('user/<int:user_id>/profile/', ProfileDetailView.as_view(), name='profile'),
    path("channel/new/", ChannelCreateView.as_view(), name="channel_new"),
]
