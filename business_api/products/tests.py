from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Product
import uuid  # Import to generate unique values

class ProductAPITest(TestCase):
    def setUp(self):
        Product.objects.all().delete()  # Clear database
        self.client = APIClient()
        self.product_data = {
            "name": "Test Product",
            "category": "Electronics",
            "price": 49.99,
            "stock_status": "in_stock",
            "sku": str(uuid.uuid4()),  # Generates a unique SKU
            "description": "A sample product for testing."
        }
        self.product = Product.objects.create(**self.product_data)

    def test_create_product(self):
        """Test API can create a product"""
        unique_product_data = self.product_data.copy()
        unique_product_data["sku"] = str(uuid.uuid4())  # Generate a new unique SKU
        response = self.client.post("/api/v1/products/", unique_product_data, format='json')
        print("POST DATA:", unique_product_data)  # Debugging input
        print("RESPONSE DATA:", response.data)  # Debugging output
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
        update_data = {
            "name": self.product_data["name"],
            "category": self.product_data["category"],
            "price": 59.99,  # Updated price
            "stock_status": self.product_data["stock_status"],
            "sku": self.product_data["sku"],  # Ensure the SKU remains the same
            "description": self.product_data["description"],
        }
        response = self.client.put(f"/api/v1/products/{self.product.id}/", update_data, format='json')
        print("UPDATE RESPONSE DATA:", response.data)  # Debugging output
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_product(self):
        """Test API can delete a product"""
        response = self.client.delete(f"/api/v1/products/{self.product.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
