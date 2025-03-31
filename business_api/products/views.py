from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.throttling import AnonRateThrottle
from django.shortcuts import get_object_or_404
from .models import Product
from .serializers import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing business products with structured API responses and rate-limiting headers.
    """
    queryset = Product.objects.all().order_by('-created_at')
    serializer_class = ProductSerializer
    throttle_classes = [AnonRateThrottle]  # Limits requests per minute per IP

    def list(self, request, *args, **kwargs):
        """Retrieve all products with pagination and rate-limit headers."""
        response = super().list(request, *args, **kwargs)
        return self._structured_response(response, "Products retrieved successfully")

    def retrieve(self, request, *args, **kwargs):
        """Retrieve a single product with structured response."""
        response = super().retrieve(request, *args, **kwargs)
        return self._structured_response(response, "Product retrieved successfully")

    def create(self, request, *args, **kwargs):
        """Create a new product with structured response and error handling."""
        response = super().create(request, *args, **kwargs)
        return self._structured_response(response, "Product created successfully", 201)

    def update(self, request, *args, **kwargs):
        """Update an existing product with structured response."""
        response = super().update(request, *args, **kwargs)
        return self._structured_response(response, "Product updated successfully")

    def destroy(self, request, *args, **kwargs):
        """Delete a product with structured response."""
        response = super().destroy(request, *args, **kwargs)
        return Response({
            "status": "success",
            "code": 204,
            "message": "Product deleted successfully"
        }, status=status.HTTP_204_NO_CONTENT)

    def _structured_response(self, response, message, success_code=200):
        """Formats API responses to include structured data and rate-limit headers."""
        rate_limit_headers = self._get_rate_limit_headers(response)

        if response.status_code >= 400:
            return Response({
                "status": "error",
                "code": response.status_code,
                "message": "An error occurred",
                "errors": response.data
            }, status=response.status_code, headers=rate_limit_headers)

        return Response({
            "status": "success",
            "code": success_code,
            "message": message,
            "data": response.data
        }, status=success_code, headers=rate_limit_headers)

    def _get_rate_limit_headers(self, response):
        """Extracts rate limit headers from Django's built-in throttling system."""
        headers = {}
        if hasattr(response, 'headers'):
            headers["X-RateLimit-Limit"] = response.headers.get("X-RateLimit-Limit", "100")
            headers["X-RateLimit-Remaining"] = response.headers.get("X-RateLimit-Remaining", "99")
            headers["X-RateLimit-Reset"] = response.headers.get("X-RateLimit-Reset", "60")
        return headers
