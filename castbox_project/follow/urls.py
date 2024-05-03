from django.urls import path
from .views import ChannelFollowView, ChannelUnfollowView


urlpatterns = [
    path("channel/<int:pk>/follow/",
         ChannelFollowView.as_view(), name="channel_follow"),
    path("channel/<int:pk>/unfollow/",
         ChannelUnfollowView.as_view(), name="channel_unfollow"),
]
