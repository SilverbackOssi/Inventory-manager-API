# Inventory Manager API

A RESTful API for managing a business's product catalog with rate limiting to prevent abuse and ensure fair usage.

## 📌 Live API URL
Base URL: [`https://inventory-manager-api-tzwk.onrender.com`](https://inventory-manager-api-tzwk.onrender.com)

## 🛠 API Documentation
- **Swagger UI**: [`/api/docs/`](https://inventory-manager-api-tzwk.onrender.com/api/docs/)
- **ReDoc UI**: [`/api/redoc/`](https://inventory-manager-api-tzwk.onrender.com/api/redoc/)

## 🔥 Postman Collection
Use Postman to test the API easily.

[![Run in Postman](https://run.pstmn.io/button.svg)](https://www.postman.com/telecoms-candidate-39964330/inventory-manager/request/3ho9fng/product-management-api?action=share&creator=43614350&ctx=documentation)

1. Click the button above OR import the collection manually.
2. Download collection: [`inventory_manager_api.postman_collection.json`](./business_api.postman_collection.json)

## 🚀 Endpoints

| Method | Endpoint | Description |
|--------|---------|-------------|
| GET    | `/api/v1/products/` | Retrieve all products |
| GET    | `/api/v1/products/{id}/` | Get details of a specific product |
| POST   | `/api/v1/products/` | Add a new product |
| PUT    | `/api/v1/products/{id}/` | Update product details |
| DELETE | `/api/v1/products/{id}/` | Delete a product |



## Features

- RESTful endpoints for CRUD operations on products
- Rate limiting (100 requests per minute per IP)
- Pagination for large collections
- Professional RESTful responses with proper status codes
- Validation for all required fields
- No authentication required (as per requirements)

## API Documentation

For full API documentation, visit our [GitHub Pages](https://SilverbackOssi.github.io/Inventory-manager-API/).

## Tech Stack

- Django 4.2
- Django REST Framework
- Python 3.10+

## Quick Start

### Prerequisites

- Python 3.10+
- pip

### Installation

1. Clone the repository
   ```sh
   git clone https://github.com/SilverbackOssi/Inventory-manager-API.git
   cd Inventory-manager-API
   ```

2. Create a virtual environment
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies
   ```sh
   pip install -r requirements.txt
   ```

4. Apply migrations
   ```sh
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Run the development server
   ```sh
   python manage.py runserver
   ```

6. Access the API at `http://localhost:8000/api/v1/products/`


## Rate Limiting

All endpoints are rate-limited to 100 requests per minute per IP address. The following headers are included in each response:

- `X-RateLimit-Limit`: The maximum number of requests allowed per time window
- `X-RateLimit-Remaining`: The number of requests remaining in the current time window
- `X-RateLimit-Reset`: Time in seconds until the rate limit is reset

## RESTful Best Practices

This API implements RESTful best practices:
- Proper use of HTTP verbs (GET, POST, PUT, DELETE)
- Resource-based URLs
- API versioning
- Consistent response format
- Appropriate HTTP status codes
- Pagination for collections
- Rate limiting with informative headers

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

