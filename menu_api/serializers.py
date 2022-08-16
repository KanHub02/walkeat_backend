from rest_framework import serializers
from .models import Fit, Category


class CategoriesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["category"]


class FitSerializer(serializers.ModelSerializer):
    category = CategoriesSerializers(many=True)

    class Meta:
        model = Fit
        fields = "__all__"
        exta_kwargs = {"price": {"read_only": True}}


class FitMenuSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=35, read_only=True)
    price = serializers.CharField(max_length=255, read_only=True)
    kcal = serializers.CharField(max_length=255, read_only=True)

    class Meta:
        model = Fit
        fields = ["title", "price", "kcal"]
