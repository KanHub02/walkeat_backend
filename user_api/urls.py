from django.urls import path, include
from .views import LoginAPIView, RegisterView, VerifyEmail, ProfileViewSet, CardViewSet
from rest_framework.routers import DefaultRouter
ROUTER = DefaultRouter()
ROUTER.register(r"profile", ProfileViewSet, basename="profile_list")
ROUTER.register(r"card", CardViewSet)


urlpatterns = [
    path('register/', RegisterView.as_view(), name="register"),
    path("login/", LoginAPIView.as_view(), name="login"),
    path('email-verify/', VerifyEmail.as_view(), name="email-verify"),
    path('', include(ROUTER.urls)),
]
