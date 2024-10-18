import requests
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

BACKEND_URL = 'http://localhost:8002/api'


@api_view(['POST'])
def send_message(request):
    """Отправка сообщения"""
    data = request.data
    response = requests.post(f"{BACKEND_URL}/message/send/", json=data)

    if response.status_code == 200:
        return Response(response.json(), status=status.HTTP_200_OK)
    else:
        return Response({'error': 'Бэкенд вернул ошибку', 'details': response.text}, status=response.status_code)
