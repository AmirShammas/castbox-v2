from django.urls import path
from .views import ProfilePlaylistDeleteView, ProfilePlaylistUpdateView, ProfilePlaylistDetailView, ProfilePlaylistCreateView, ChannelUnfollowView, ChannelFollowView, EpisodeUnlikeView, EpisodeLikeView, EpisodeDetailView, ProfileEpisodeDeleteView, ProfileEpisodeUpdateView, ProfileEpisodeDetailView, ProfileEpisodeCreateView, ProfileChannelCreateView, ChannelDetailView, ChannelListView, ProfileChannelDeleteView, ProfileChannelUpdateView, CommentCreateView, EpisodeListView, ProfileChannelDetailView, ProfileDetailView, SignupPageView, HomePageView

urlpatterns = [
    path("accounts/signup/", SignupPageView.as_view(), name="signup"),
    path("", HomePageView.as_view(), name="home"),
    path("channel/", ChannelListView.as_view(), name="channel_list"),
    path("channel/<int:pk>/", ChannelDetailView.as_view(), name="channel_detail"),
    path("channel/<int:pk>/follow", ChannelFollowView.as_view(), name="channel_follow"),
    path("channel/<int:pk>/unfollow", ChannelUnfollowView.as_view(), name="channel_unfollow"),
    path("channel/<int:channel_id>/episode/", EpisodeListView.as_view(), name="episode_list"),
    path("channel/<int:channel_id>/comment/", CommentCreateView.as_view(), name="comment_new"),
    path("channel/<int:channel_id>/episode/<int:pk>/", EpisodeDetailView.as_view(), name="episode_detail"),
    path("channel/<int:channel_id>/episode/<int:pk>/like", EpisodeLikeView.as_view(), name='episode_like'),
    path("channel/<int:channel_id>/episode/<int:pk>/unlike", EpisodeUnlikeView.as_view(), name='episode_unlike'),
    path("profile/<int:pk>/", ProfileDetailView.as_view(), name='profile'),
    path("profile/<int:profile_id>/channel/<int:pk>/", ProfileChannelDetailView.as_view(), name='profile_channel_detail'),
    path("profile/<int:profile_id>/channel/new/", ProfileChannelCreateView.as_view(), name="profile_channel_new"),
    path("profile/<int:profile_id>/channel/<int:pk>/edit/", ProfileChannelUpdateView.as_view(), name="profile_channel_edit"),
    path("profile/<int:profile_id>/channel/<int:pk>/delete/", ProfileChannelDeleteView.as_view(), name="profile_channel_delete"),
    path("profile/<int:profile_id>/channel/<int:channel_id>/episode/new/", ProfileEpisodeCreateView.as_view(), name="profile_episode_new"),
    path("profile/<int:profile_id>/channel/<int:channel_id>/episode/<int:pk>/", ProfileEpisodeDetailView.as_view(), name="profile_episode_detail"),
    path("profile/<int:profile_id>/channel/<int:channel_id>/episode/<int:pk>/edit/", ProfileEpisodeUpdateView.as_view(), name="profile_episode_edit"),
    path("profile/<int:profile_id>/channel/<int:channel_id>/episode/<int:pk>/delete/", ProfileEpisodeDeleteView.as_view(), name="profile_episode_delete"),
    path("profile/<int:profile_id>/playlist/new/", ProfilePlaylistCreateView.as_view(), name="profile_playlist_new"),
    path("profile/<int:profile_id>/playlist/<int:pk>/", ProfilePlaylistDetailView.as_view(), name='profile_playlist_detail'),
    path("profile/<int:profile_id>/playlist/<int:pk>/edit/", ProfilePlaylistUpdateView.as_view(), name="profile_playlist_edit"),
    path("profile/<int:profile_id>/playlist/<int:pk>/delete/", ProfilePlaylistDeleteView.as_view(), name="profile_playlist_delete"),
]
