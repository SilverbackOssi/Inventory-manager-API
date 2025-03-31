# Product Management API Documentation

## Overview

This API provides endpoints for managing a business's product catalog with rate limiting to ensure fair usage. It supports CRUD operations (Create, Read, Update, Delete) for products and manages product stock availability.

## Base URL

```
https://inventory-manager-api-tzwk.onrender.com
```

## Rate Limiting

All endpoints are rate-limited to 100 requests per minute per IP address. The following headers are included in each response to inform you about your current rate limit status:

- `X-RateLimit-Limit`: The maximum number of requests allowed per time window
- `X-RateLimit-Remaining`: The number of requests remaining in the current time window
- `X-RateLimit-Reset`: Time in seconds until the rate limit is reset

## Endpoints

### 1. Get All Products

Retrieves a paginated list of all products.

- **URL**: `/api/v1/products`
- **Method**: `GET`
- **URL Parameters**:
  - `page=[integer]` (optional): Specify the page number for pagination

#### Success Response

- **Code**: `200 OK`
- **Content Example**:

```json
{
  "status": "success",
  "code": 200,
  "message": "Products retrieved successfully",
  "data": {
    "products": [
      {
        "id": "P001",
        "name": "Wireless Mouse",
        "category": "Electronics",
        "price": 29.99,
        "stock_status": "in_stock",
        "sku": "WM-001",
        "description": "A high-precision wireless mouse with ergonomic design.",
        "created_at": "2024-10-20T15:32:45Z",
        "updated_at": "2024-10-21T10:15:30Z"
      },
      {
        "id": "P002",
        "name": "Office Chair",
        "category": "Furniture",
        "price": 89.99,
        "stock_status": "out_of_stock",
        "sku": "OC-002",
        "description": "An ergonomic office chair with lumbar support.",
        "created_at": "2024-10-01T09:00:00Z",
        "updated_at": "2024-10-16T12:45:15Z"
      }
    ],
    "pagination": {
      "current_page": 1,
      "per_page": 10,
      "total_pages": 3,
      "total_products": 25
    }
  },
  "links": {
    "self": "/api/v1/products?page=1",
    "next": "/api/v1/products?page=2",
    "prev": null
  }
}
```

### 2. Get a Specific Product

Retrieves details for a specific product by ID.

- **URL**: `/api/v1/products/{id}`
- **Method**: `GET`
- **URL Parameters**:
  - `id=[string]` (required): Product ID

#### Success Response

- **Code**: `200 OK`
- **Content Example**:

```json
{
  "status": "success",
  "code": 200,
  "message": "Product details retrieved successfully",
  "data": {
    "product": {
      "id": "P001",
      "name": "Wireless Mouse",
      "category": "Electronics",
      "price": 29.99,
      "stock_status": "in_stock",
      "sku": "WM-001",
      "description": "A high-precision wireless mouse with ergonomic design.",
      "created_at": "2024-10-20T15:32:45Z",
      "updated_at": "2024-10-21T10:15:30Z"
    }
  }
}
```

#### Error Response

- **Code**: `404 Not Found`
- **Content Example**:

```json
{
  "status": "error",
  "code": 404,
  "message": "Product not found",
  "errors": {
    "details": "No product was found with the given ID."
  }
}
```

### 3. Create a New Product

Adds a new product to the catalog.

- **URL**: `/api/v1/products/`
- **Method**: `POST`
- **Content-Type**: `application/json`
- **Body**:

```json
{
  "id": "P003",
  "name": "Mechanical Keyboard",
  "category": "Electronics",
  "price": 59.99,
  "stock_status": "in_stock",
  "sku": "MK-003",
  "description": "A mechanical keyboard with RGB lighting and tactile switches."
}
```

#### Success Response

- **Code**: `201 Created`
- **Content Example**:

```json
{
  "status": "success",
  "code": 200,
  "message": "Product created successfully",
  "data": {
    "product": {
      "id": "P003",
      "name": "Mechanical Keyboard",
      "category": "Electronics",
      "price": 59.99,
      "stock_status": "in_stock",
      "sku": "MK-003",
      "description": "A mechanical keyboard with RGB lighting and tactile switches.",
      "created_at": "2024-10-22T14:30:45Z",
      "updated_at": "2024-10-22T14:30:45Z"
    }
  }
}
```

#### Error Response

- **Code**: `400 Bad Request`
- **Content Example**:

```json
{
  "status": "error",
  "code": 400,
  "message": "Validation error",
  "errors": {
    "details": {
      "price": ["Ensure this value is greater than or equal to 0.01."]
    }
  }
}
```

### 4. Update a Product

Updates an existing product's information.

- **URL**: `/api/v1/products/{id}`
- **Method**: `PUT`
- **URL Parameters**:
  - `id=[string]` (required): Product ID
- **Content-Type**: `application/json`
- **Body**:

```json
{
  "name": "Wireless Ergonomic Mouse",
  "price": 34.99,
  "stock_status": "low_stock"
}
```

#### Success Response

- **Code**: `200 OK`
- **Content Example**:

```json
{
  "status": "success",
  "code": 200,
  "message": "Product updated successfully",
  "data": {
    "product": {
      "id": "P001",
      "name": "Wireless Ergonomic Mouse",
      "category": "Electronics",
      "price": 34.99,
      "stock_status": "low_stock",
      "sku": "WM-001",
      "description": "A high-precision wireless mouse with ergonomic design.",
      "created_at": "2024-10-20T15:32:45Z",
      "updated_at": "2024-10-22T16:45:20Z"
    }
  }
}
```

#### Error Response

- **Code**: `404 Not Found`
- **Content Example**:

```json
{
  "status": "error",
  "code": 404,
  "message": "Product not found",
  "errors": {
    "details": "No product was found with the given ID."
  }
}
```

### 5. Delete a Product

Removes a product from the catalog.

- **URL**: `/api/v1/products/{id}`
- **Method**: `DELETE`
- **URL Parameters**:
  - `id=[string]` (required): Product ID

#### Success Response

- **Code**: `200 OK`
- **Content Example**:

```json
{
  "status": "success",
  "code": 200,
  "message": "Product deleted successfully"
}
```

#### Error Response

- **Code**: `404 Not Found`
- **Content Example**:

```json
{
  "status": "error",
  "code": 404,
  "message": "Product not found",
  "errors": {
    "details": "No product was found with the given ID."
  }
}
```

## Testing with Postman

1. Download and import the [Postman collection](./business_api.postman_collection.json)
2. Set up environment variables if needed
3. Test each endpoint with the provided examples

## Setup and Installation

1. Clone the repository
   ```
   git clone https://github.com/SilverbackOssi/Inventory-manager-API.git
   cd Inventory-manager-API
   ```

2. Install dependencies
   ```
   pip install -r requirements.txt
   ```

3. Apply migrations
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```

4. Run the development server
   ```
   python manage.py runserver
   ```

5. Then access the API at `http://localhost:8000/api/v1/products/`