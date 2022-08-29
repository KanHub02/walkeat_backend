from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse

from .models import Fit, Category, Cart


class FitTests(APITestCase):
    def test_fit_list(self):
        response = self.client.get(reverse("detail_fit_api"))
        print(response)
# Create your tests here.
