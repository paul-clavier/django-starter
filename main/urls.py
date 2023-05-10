from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views

app_name = "main"

router = DefaultRouter()
router.register(
    r"masterdatapoints", views.MasterDatapointViewset, basename="masterdatapoints"
)
urlpatterns = [
    path("", include(router.urls)),
]
