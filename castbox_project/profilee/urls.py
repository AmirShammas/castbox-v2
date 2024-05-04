from django.urls import path
from .views import ProfileCommentDeleteView, ProfileCommentUpdateView, ProfileCommentDetailView, ProfilePlaylistEpisodeDeleteView, ProfilePlaylistDeleteView, ProfilePlaylistUpdateView, ProfilePlaylistDetailView, ProfilePlaylistCreateView, ProfileEpisodeDeleteView, ProfileEpisodeUpdateView, ProfileEpisodeDetailView, ProfileEpisodeCreateView, ProfileChannelCreateView, ProfileChannelDeleteView, ProfileChannelUpdateView, ProfileChannelDetailView, ProfileDetailView


urlpatterns = [
    path("profile/<int:pk>/", ProfileDetailView.as_view(), name='profile'),
    path("profile/<int:profile_id>/channel/<int:pk>/",
         ProfileChannelDetailView.as_view(), name="profile_channel_detail"),
    path("profile/<int:profile_id>/channel/new/",
         ProfileChannelCreateView.as_view(), name="profile_channel_new"),
    path("profile/<int:profile_id>/channel/<int:pk>/edit/",
         ProfileChannelUpdateView.as_view(), name="profile_channel_edit"),
    path("profile/<int:profile_id>/channel/<int:pk>/delete/",
         ProfileChannelDeleteView.as_view(), name="profile_channel_delete"),
    path("profile/<int:profile_id>/channel/<int:channel_id>/comment/<int:pk>/",
         ProfileCommentDetailView.as_view(), name="profile_comment_detail"),
    path("profile/<int:profile_id>/channel/<int:channel_id>/comment/<int:pk>/edit/",
         ProfileCommentUpdateView.as_view(), name="profile_comment_edit"),
    path("profile/<int:profile_id>/channel/<int:channel_id>/comment/<int:pk>/delete/",
         ProfileCommentDeleteView.as_view(), name="profile_comment_delete"),
    path("profile/<int:profile_id>/channel/<int:channel_id>/episode/new/",
         ProfileEpisodeCreateView.as_view(), name="profile_episode_new"),
    path("profile/<int:profile_id>/channel/<int:channel_id>/episode/<int:pk>/",
         ProfileEpisodeDetailView.as_view(), name="profile_episode_detail"),
    path("profile/<int:profile_id>/channel/<int:channel_id>/episode/<int:pk>/edit/",
         ProfileEpisodeUpdateView.as_view(), name="profile_episode_edit"),
    path("profile/<int:profile_id>/channel/<int:channel_id>/episode/<int:pk>/delete/",
         ProfileEpisodeDeleteView.as_view(), name="profile_episode_delete"),
    path("profile/<int:profile_id>/playlist/new/",
         ProfilePlaylistCreateView.as_view(), name="profile_playlist_new"),
    path("profile/<int:profile_id>/playlist/<int:pk>/",
         ProfilePlaylistDetailView.as_view(), name="profile_playlist_detail"),
    path("profile/<int:profile_id>/playlist/<int:pk>/edit/",
         ProfilePlaylistUpdateView.as_view(), name="profile_playlist_edit"),
    path("profile/<int:profile_id>/playlist/<int:pk>/delete/",
         ProfilePlaylistDeleteView.as_view(), name="profile_playlist_delete"),
    path("profile/<int:profile_id>/playlist/<int:pk>/episode/<int:episode_id>/delete/",
         ProfilePlaylistEpisodeDeleteView.as_view(), name="profile_playlist_episode_delete"),
]