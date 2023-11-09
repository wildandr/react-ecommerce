from pyramid.view import view_config
from pyramid.response import Response
import json

products = [
    {"id": 1, "name": "Product 1", "price": 20.0},
    {"id": 2, "name": "Product 2", "price": 30.0},
    # Add more products as needed
]

@view_config(route_name='products', renderer='json')
def get_products(request):
    return products

@view_config(route_name='product', renderer='json')
def get_product(request):
    product_id = int(request.matchdict['id'])
    product = next((p for p in products if p["id"] == product_id), None)
    if product:
        return product
    else:
        return Response(json.dumps({"error": "Product not found"}), status_code=404)
