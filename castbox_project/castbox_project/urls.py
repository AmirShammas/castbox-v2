from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path("", include("castbox.urls")),
    path("", include("channel.urls")),
    path("", include("comment.urls")),
    path("", include("follow.urls")),
]
