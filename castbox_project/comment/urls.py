from django.urls import path
from .views import CommentCreateView


urlpatterns = [
    path("channel/<int:channel_id>/comment/",
         CommentCreateView.as_view(), name="comment_new"),
]
