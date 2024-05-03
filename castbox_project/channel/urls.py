from django.urls import include, path
from .views import ChannelListView, ChannelDetailView


urlpatterns = [
    path("channel/", ChannelListView.as_view(), name="channel_list"),
    path("channel/<int:pk>/", ChannelDetailView.as_view(), name="channel_detail"),
]
