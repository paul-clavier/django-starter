from django.contrib.auth.views import LogoutView
from django.urls import path, include

from rest_framework.routers import DefaultRouter
from . import views

app_name = "authentication"

router = DefaultRouter()
router.register(r"users", views.UserViewset, basename="users")
router.register(r"access-tokens", views.TokenViewset, basename="access_tokens")

urlpatterns = [
    path("", include(router.urls)),
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
]
