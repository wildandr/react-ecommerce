from pyramid.view import view_config
from pyramid.response import Response
import json

orders = [
    {"id": 1, "product_id": 1, "quantity": 2, "total_price": 40.0},
    {"id": 2, "product_id": 2, "quantity": 1, "total_price": 30.0},
    # Add more orders as needed
]

@view_config(route_name='orders', renderer='json')
def get_orders(request):
    return orders

@view_config(route_name='order', renderer='json')
def get_order(request):
    order_id = int(request.matchdict['id'])
    order = next((o for o in orders if o["id"] == order_id), None)
    if order:
        return order
    else:
        return Response(json.dumps({"error": "Order not found"}), status_code=404)
