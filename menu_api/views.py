from django.shortcuts import render
from .serializers import FitSerializer, FitMenuSerializer, CategoriesSerializers
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from .models import Fit, Category
from django.shortcuts import get_object_or_404
from rest_framework.response import Response


class FitViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated, IsAdminUser]
    queryset = Fit.objects.all()
    serializer_class = FitSerializer


class FitMenuView(ListAPIView):
    permission_classes = [IsAuthenticated,]
    serializer_class = FitMenuSerializer
    queryset = Fit.objects.all()

class FitByCategoryApiView(APIView):
    permission_classes = [AllowAny,]
    serializer_class = FitSerializer
    def get(self, request, category):
        fit = get_object_or_404(Fit, category=category)
        likes_data = self.serializer_class(fit.category, many=True, context={"request": request}
        ).data
        return Response(data=likes_data)


class CategoryView(ListAPIView):
    permission_classes = [AllowAny, ]
    serializer_class = CategoriesSerializers
    queryset = Category.objects.all()




