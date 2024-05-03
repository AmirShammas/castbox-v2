from django.urls import path
from .views import LogListView


urlpatterns = [
    path("log/", LogListView.as_view(), name="log_list"),
]
