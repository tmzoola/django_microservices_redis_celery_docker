from django.http import JsonResponse


def healthcheck(request):
    return JsonResponse({'status': 'ok'})


def hello(request):
    return JsonResponse({'hello': 'world'})


def index(request):
    return JsonResponse({"message": "Index world!"})