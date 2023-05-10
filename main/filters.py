from django_filters.rest_framework import FilterSet

from main.models import MasterDatapoint


class MasterDatapointFilterSet(FilterSet):
    class Meta:
        model = MasterDatapoint
        fields = ["name"]
