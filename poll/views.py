from django.http import JsonResponse
from rest_framework.decorators import api_view


@api_view(['GET'])
def index(request):
    if request.method == 'GET':
        return JsonResponse(data={'message': 'Hello World'}, status=200)
