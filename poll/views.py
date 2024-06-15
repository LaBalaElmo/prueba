from django.http import JsonResponse
from rest_framework.decorators import api_view


@api_view(['GET'])
def index(request):
    if request.method == 'GET':
        return JsonResponse(data={'message': 'Hello From Django'}, status=200)


@api_view(['POST'])
def create(request):
    if request.method == 'POST':
        print(request.data)
        return JsonResponse(data=request.data, status=200)
