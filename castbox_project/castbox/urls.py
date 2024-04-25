from django.urls import path
from .views import ProfileChannelCreateView, ChannelDetailView, ChannelListView, ProfileChannelUpdateView, CommentCreateView, EpisodeListView, ProfileChannelDetailView, ProfileDetailView, SignupPageView, HomePageView

urlpatterns = [
    path("accounts/signup/", SignupPageView.as_view(), name="signup"),
    path("", HomePageView.as_view(), name="home"),
    path("channel/", ChannelListView.as_view(), name="channel_list"),
    path("channel/<int:pk>/", ChannelDetailView.as_view(), name="channel_detail"),
    path("channel/<int:channel_id>/episode/", EpisodeListView.as_view(), name="episode_list"),
    path("channel/<int:channel_id>/comment/", CommentCreateView.as_view(), name="comment_new"),
    path('user/<int:user_id>/profile/', ProfileDetailView.as_view(), name='profile'),
    path('profile/channel/<int:pk>/', ProfileChannelDetailView.as_view(), name='profile_channel_detail'),
    path("profile/channel/new/", ProfileChannelCreateView.as_view(), name="profile_channel_new"),
    path("profile/channel/<int:pk>/edit/", ProfileChannelUpdateView.as_view(), name="profile_channel_edit"),
]
