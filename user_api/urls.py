from django.urls import path, include
from .views import UserViewSet, LoginAPIView
from rest_framework.routers import DefaultRouter

ROUTER = DefaultRouter()
ROUTER.register(r"account", UserViewSet)

urlpatterns = [
    path("", include(ROUTER.urls)),
    path("login/", LoginAPIView.as_view(), name="login"),
]
