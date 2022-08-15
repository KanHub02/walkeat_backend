from django.urls import path, include
from .views import FitViewSet, FitMenuView, CategoryView, FitByCategoryApiView
from rest_framework.routers import DefaultRouter, SimpleRouter

ROUTER = SimpleRouter()
ROUTER.register(r"menu", FitViewSet)

urlpatterns = [
    path("", include(ROUTER.urls), name="menu_api"),
    path("main-menu/", FitMenuView.as_view(), name="main_menu_api"),
    path("main-menu/categories", CategoryView.as_view(), name="categories_api"),
]