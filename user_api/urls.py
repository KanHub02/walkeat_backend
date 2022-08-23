from django.urls import path, include
from .views import LoginAPIView, RegisterView, VerifyEmail
from rest_framework.routers import DefaultRouter



urlpatterns = [
    path('register/', RegisterView.as_view(), name="register"),
    path("login/", LoginAPIView.as_view(), name="login"),
    path('email-verify/', VerifyEmail.as_view(), name="email-verify"),
]
