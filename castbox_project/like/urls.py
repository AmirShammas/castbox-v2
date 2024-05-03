from django.urls import path
from .views import EpisodeLikeView, EpisodeUnlikeView


urlpatterns = [
    path("channel/<int:channel_id>/episode/<int:pk>/like/",
         EpisodeLikeView.as_view(), name="episode_like"),
    path("channel/<int:channel_id>/episode/<int:pk>/unlike/",
         EpisodeUnlikeView.as_view(), name="episode_unlike"),
]
