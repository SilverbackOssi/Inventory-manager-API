from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Product

class ProductAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.product_data = {
            "name": "Test Product",
            "category": "Electronics",
            "price": 49.99,
            "stock_status": "in_stock",
            "sku": "TP-001",
            "description": "A sample product for testing."
        }
        self.product = Product.objects.create(**self.product_data)

    def test_create_product(self):
        """Test API can create a product"""
        response = self.client.post("/api/v1/products/", self.product_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_product_list(self):
        """Test API can retrieve product list"""
        response = self.client.get("/api/v1/products/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_product_detail(self):
        """Test API can retrieve a specific product"""
        response = self.client.get(f"/api/v1/products/{self.product.id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_product(self):
        """Test API can update a product"""
        update_data = {"price": 59.99}
        response = self.client.put(f"/api/v1/products/{self.product.id}/", update_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_product(self):
        """Test API can delete a product"""
        response = self.client.delete(f"/api/v1/products/{self.product.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
