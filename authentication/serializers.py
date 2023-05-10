from datetime import datetime

from django.contrib.auth.password_validation import validate_password
from django.contrib.sessions.models import Session
from rest_framework import serializers

from authentication.models import User, AccessToken


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, required=False, validators=[validate_password]
    )

    @staticmethod
    def _set_password(user: User, validated_data: dict):
        if "password" in validated_data:
            user.set_password(validated_data["password"])
            user.save()

    @staticmethod
    def _remove_user_sessions_if_inactive(user: User, validated_data: dict):
        """Ensures the user is logged out when set to inactive"""
        if not validated_data.get("is_active", True):
            user_sessions = [
                session.pk
                for session in Session.objects.filter(expire_date__gte=datetime.now())
                if str(user.pk) == session.get_decoded().get("_auth_user_id")
            ]
            Session.objects.filter(pk__in=user_sessions).delete()

    def create(self, validated_data):
        user = super().create(validated_data)
        self._set_password(user, validated_data)
        return user

    def update(self, user, validated_data):
        super().update(user, validated_data)
        self._set_password(user, validated_data)
        self._remove_user_sessions_if_inactive(user, validated_data)
        return user

    class Meta:
        model = User
        fields = "__all__"


class AccessTokenSerializer(serializers.ModelSerializer):
    token = serializers.CharField(read_only=True)

    class Meta:
        model = AccessToken
        fields = ["id", "token", "user"]
