from pyramid.view import view_config
from pyramid.response import Response
import json

payments = [
    {"id": 1, "name": "Payment Gateway 1", "enabled": True},
    {"id": 2, "name": "Payment Gateway 2", "enabled": False},
    # Add more payment gateways as needed
]

@view_config(route_name='payments', renderer='json')
def get_payments(request):
    return payments

@view_config(route_name='payment', renderer='json')
def get_payment(request):
    payment_id = int(request.matchdict['id'])
    payment = next((p for p in payments if p["id"] == payment_id), None)
    if payment:
        return payment
    else:
        return Response(json.dumps({"error": "Payment gateway not found"}), status_code=404)
