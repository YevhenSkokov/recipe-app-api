from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import TestCase

# from rest_framework import status
# from rest_framework.test import APIClient

# from core.models import Ingredient

# from recipe.serializers import IngredientSerializer


# INGREDIENTS_URL = reverse('recipe:ingredient-list')


# class PublicIngredientsAPITest(TestCase):
#     """Test the publicly available ingredients API"""

#     def setUp(self):
#         self.client = APIClient()

#     def test_login_required(self):
#         """Test that login is required to access the endpoint"""
#         res =  self.client.get(INGREDIENTS_URL)

#         self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)
