import requests
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

BACKEND_URL = "http://localhost:8001/api"


@api_view(["GET"])
def get_chats(request):
    """Получение списка чатов"""
    response = requests.get(f"{BACKEND_URL}/chats/all/", params=request.query_params)

    if response.status_code == 200:
        return Response(response.json(), status=status.HTTP_200_OK)
    else:
        return Response({"error": "Бэкенд вернул ошибку", "details": response.text}, status=response.status_code)
