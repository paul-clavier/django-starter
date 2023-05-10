from rest_framework import serializers

from .models import MasterDatapoint


class MasterDatapointSerializer(serializers.ModelSerializer):
    class Meta:
        model = MasterDatapoint
        fields = "__all__"
