from django.http import JsonResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    return JsonResponse({'message': 'Hello from mailing project'})
