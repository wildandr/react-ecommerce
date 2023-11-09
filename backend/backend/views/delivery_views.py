from pyramid.view import view_config
from pyramid.response import Response
import json

deliveries = [
    {"id": 1, "name": "Delivery Service 1", "enabled": True},
    {"id": 2, "name": "Delivery Service 2", "enabled": False},
    # Add more delivery services as needed
]

@view_config(route_name='deliveries', renderer='json')
def get_deliveries(request):
    return deliveries

@view_config(route_name='delivery', renderer='json')
def get_delivery(request):
    delivery_id = int(request.matchdict['id'])
    delivery = next((d for d in deliveries if d["id"] == delivery_id), None)
    if delivery:
        return delivery
    else:
        return Response(json.dumps({"error": "Delivery service not found"}), status_code=404)
