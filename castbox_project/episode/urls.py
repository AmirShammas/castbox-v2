from django.urls import path
from .views import EpisodeListView, EpisodeDetailView, EpisodePlayView


urlpatterns = [
    path("channel/<int:channel_id>/episode/",
         EpisodeListView.as_view(), name="episode_list"),
    path("channel/<int:channel_id>/episode/<int:pk>/",
         EpisodeDetailView.as_view(), name="episode_detail"),
    path("channel/<int:channel_id>/episode/<int:pk>/play/",
         EpisodePlayView.as_view(), name="episode_play"),
]
