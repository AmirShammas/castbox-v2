from django.urls import path
from .views import EpisodeSelectPlaylistView


urlpatterns = [
    path("channel/<int:channel_id>/episode/<int:pk>/select-playlist/",
         EpisodeSelectPlaylistView.as_view(), name="episode_select_playlist"),
]
