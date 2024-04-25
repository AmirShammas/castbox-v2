from django.urls import path
from .views import ProfileEpisodeDeleteView, ProfileEpisodeUpdateView, ProfileEpisodeDetailView, ProfileEpisodeCreateView, ProfileChannelCreateView, ChannelDetailView, ChannelListView, ProfileChannelDeleteView, ProfileChannelUpdateView, CommentCreateView, EpisodeListView, ProfileChannelDetailView, ProfileDetailView, SignupPageView, HomePageView

urlpatterns = [
    path("accounts/signup/", SignupPageView.as_view(), name="signup"),
    path("", HomePageView.as_view(), name="home"),
    path("channel/", ChannelListView.as_view(), name="channel_list"),
    path("channel/<int:pk>/", ChannelDetailView.as_view(), name="channel_detail"),
    path("channel/<int:channel_id>/episode/", EpisodeListView.as_view(), name="episode_list"),
    path("channel/<int:channel_id>/comment/", CommentCreateView.as_view(), name="comment_new"),
    path('profile/<int:pk>/', ProfileDetailView.as_view(), name='profile'),
    path('profile/<int:profile_id>/channel/<int:pk>/', ProfileChannelDetailView.as_view(), name='profile_channel_detail'),
    path("profile/<int:profile_id>/channel/new/", ProfileChannelCreateView.as_view(), name="profile_channel_new"),
    path("profile/<int:profile_id>/channel/<int:pk>/edit/", ProfileChannelUpdateView.as_view(), name="profile_channel_edit"),
    path("profile/<int:profile_id>/channel/<int:pk>/delete/", ProfileChannelDeleteView.as_view(), name="profile_channel_delete"),
    path("profile/channel/<int:channel_id>/episode/new/", ProfileEpisodeCreateView.as_view(), name="profile_episode_new"),
    path("profile/channel/<int:channel_id>/episode/<int:pk>/", ProfileEpisodeDetailView.as_view(), name="profile_episode_detail"),
    path("profile/channel/<int:channel_id>/episode/<int:pk>/edit/", ProfileEpisodeUpdateView.as_view(), name="profile_episode_edit"),
    path("profile/channel/<int:channel_id>/episode/<int:pk>/delete/", ProfileEpisodeDeleteView.as_view(), name="profile_episode_delete"),
]
