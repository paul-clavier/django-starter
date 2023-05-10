from django.utils.translation import gettext_lazy as _
from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.permissions import DjangoModelPermissions

from authentication.models import AccessToken


class AccessTokenAuthentication(TokenAuthentication):
    """
    Token based authentication.

    Clients should authenticate by passing the token key in the "Authorization"
    HTTP header, prepended with the string "Token ".  For example:

        Authorization: Token 401f7ac837da42b97f613d789819ff93537bee6a

    Tokens can be generated for a specific user by an admin on the `access-tokens`
    endpoint.
    """

    def authenticate_credentials(self, key: str):
        try:
            token_id, fingerprint = key.split(".")
            token: AccessToken = AccessToken.objects.select_related("user").get(
                token_id=token_id
            )
        except Exception:
            raise AuthenticationFailed(_("Invalid token."))

        if not token.check_fingerprint(fingerprint):
            raise AuthenticationFailed(_("Invalid token."))

        if not token.user.is_active:
            raise AuthenticationFailed(_("User inactive or deleted."))

        return token.user, token


class RestrictedDjangoModelPermissions(DjangoModelPermissions):
    perms_map = {
        **DjangoModelPermissions.perms_map,
        "GET": ["%(app_label)s.view_%(model_name)s"],
        "HEAD": ["%(app_label)s.view_%(model_name)s"],
    }
