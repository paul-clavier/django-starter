from django.contrib.auth.views import LoginView as DefaultLoginView
from django.http import JsonResponse
from rest_framework import status, viewsets
from rest_framework.mixins import CreateModelMixin
from rest_framework.viewsets import GenericViewSet

from authentication.models import User, AccessToken
from .serializers import (
    UserSerializer,
    AccessTokenSerializer,
)


class UserViewset(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.prefetch_related("groups", "user_permissions").all()
    search_fields = ["email", "first_name", "last_name"]
    ordering = ["id"]


class TokenViewset(
    CreateModelMixin,
    GenericViewSet,
):
    serializer_class = AccessTokenSerializer
    queryset = AccessToken.objects.all()


class LoginView(DefaultLoginView):
    """
    This view overrides the default behaviour of the Login view to provide
    better integration with JavaScript application. The statuses are now 200
    when login is successful and 401 when not successful to indicate the result
    to the JavaScript application.

    To keep the correct behaviour with the swagger, the status code is kept
    the same (redirect) when login is successful and a redirect url is
    provided.
    """

    def form_valid(self, form):
        response = super().form_valid(form)
        if not self.get_redirect_url():
            return JsonResponse({})
        return response

    def form_invalid(self, form):
        response = super().form_invalid(form)
        response.status_code = status.HTTP_401_UNAUTHORIZED
        return response
