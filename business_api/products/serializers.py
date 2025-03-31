from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    """Serializer for Product model with robust validation and formatted response."""

    class Meta:
        model = Product
        fields = [
            'id', 'name', 'category', 'price', 'stock_status', 
            'sku', 'description', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']  # Prevent changes to these fields

    def validate_name(self, value):
        """Ensure product name is at least 3 characters long."""
        if len(value) < 3:
            raise serializers.ValidationError("Product name must be at least 3 characters long.")
        return value

    def validate_price(self, value):
        """Ensure price is positive."""
        if value <= 0:
            raise serializers.ValidationError("Price must be greater than zero.")
        return value

    def validate_category(self, value):
        """Ensure category is not empty."""
        if not value.strip():
            raise serializers.ValidationError("Category cannot be empty.")
        return value
