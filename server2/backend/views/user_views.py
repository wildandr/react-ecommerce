from pyramid.view import view_config
from pyramid.response import Response
import json

users = [
    {"id": 1, "username": "user1", "email": "user1@example.com"},
    {"id": 2, "username": "user2", "email": "user2@example.com"},
    # Add more users as needed
]

@view_config(route_name='users', renderer='json')
def get_users(request):
    return users

@view_config(route_name='user', renderer='json')
def get_user(request):
    user_id = int(request.matchdict['id'])
    user = next((u for u in users if u["id"] == user_id), None)
    if user:
        return user
    else:
        return Response(json.dumps({"error": "User not found"}), status_code=404)
