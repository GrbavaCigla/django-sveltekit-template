import requests

from django.conf import settings
from django.shortcuts import redirect

from rest_framework.views import APIView, Response


class UserActivation(APIView):
    def get(self, request, uid, token):
        payload = {"uid": uid, "token": token}

        url = request.build_absolute_uri("/api/v1/auth/users/activation/")
        response = requests.post(url, data=payload)

        if response.ok:
            return redirect(settings.ACTIVATION_REDIRECT)

        return Response(response.content)
