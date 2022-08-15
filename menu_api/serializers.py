from rest_framework import serializers
from .models import Fit, Category


class FitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fit
        fields = "__all__"
        exta_kwargs = {
            "price": {
                "read_only": True
            }
        }


class FitMenuSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=35, read_only=True)
    price = serializers.CharField(max_length=255, read_only=True)
    kcal = serializers.CharField(max_length=255, read_only=True)

    class Meta:
        model = Fit
        fields = ["title", "price", "kcal"]


class CategoriesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

    # def to_representation(self, instance):
    #     super(CategoriesSerializers, self).to_representation(instance)