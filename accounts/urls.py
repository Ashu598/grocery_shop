from django.urls import path
from .views import signup, SignInView, SignOutView, profile

urlpatterns = [
    path("signup/", signup, name="signup"),
    path("login/", SignInView.as_view(), name="login"),
    path("logout/", SignOutView.as_view(), name="logout"),
    path("profile/", profile, name="profile"),
]
