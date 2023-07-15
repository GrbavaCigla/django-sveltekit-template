from django.urls import path, include

from drf_spectacular.views import SpectacularAPIView

from .views import UserActivation


app_name = 'api'


urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('auth/activate/<str:uid>/<str:token>/', UserActivation.as_view()),
    path('schema/', SpectacularAPIView.as_view()),
]