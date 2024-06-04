# users/urls.py

from django.urls import path
from rest_framework_simplejwt.views import ( # type: ignore
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from .views import register, logout_view

urlpatterns = [
    path("register", register, name="register"),
    path("login", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh", TokenRefreshView.as_view(), name="token_refresh"),
    path("token/verify", TokenVerifyView.as_view(), name="token_verify"),
    path("logout", logout_view, name="logout"),
]
