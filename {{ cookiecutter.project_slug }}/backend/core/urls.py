from django.urls import path, include

from drf_spectacular.views import SpectacularAPIView

app_name = "core"


urlpatterns = [
    path("schema/", SpectacularAPIView.as_view()),
    path("", include("user.urls")),
]
