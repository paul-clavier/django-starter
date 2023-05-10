from rest_framework import viewsets

from .filters import MasterDatapointFilterSet
from .models import MasterDatapoint
from .serializers import MasterDatapointSerializer


class MasterDatapointViewset(viewsets.ModelViewSet):
    serializer_class = MasterDatapointSerializer
    queryset = MasterDatapoint.objects.all()
    search_fields = ["name", "definition"]
    filterset_class = MasterDatapointFilterSet
    ordering = ["id"]
