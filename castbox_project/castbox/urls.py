from django.urls import path
from .views import SignupPageView, HomePageView


urlpatterns = [
    path("accounts/signup/", SignupPageView.as_view(), name="signup"),
    path("", HomePageView.as_view(), name="home"),
]
