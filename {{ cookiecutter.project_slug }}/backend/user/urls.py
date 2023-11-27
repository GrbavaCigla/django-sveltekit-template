from django.urls import path, include

from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView, TokenVerifyView
from drf_spectacular.views import SpectacularAPIView

from .views import UserActivation


app_name = "auth"


urlpatterns = [
    path("auth/", include("djoser.urls")),
    path(
        "auth/token/",
        TokenObtainPairView.as_view(),
        name="jwt-create",
    ),
    path(
        "auth/refresh/",
        TokenRefreshView.as_view(),
        name="jwt-refresh",
    ),
    path("auth/verify/", TokenVerifyView.as_view(), name="jwt-verify"),
    path("auth/activate/<str:uid>/<str:token>/", UserActivation.as_view()),
]
