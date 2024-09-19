from django.urls import path
from .views import healthcheck, hello, index

urlpatterns = [
    path('healthcheck/', healthcheck, name='healthcheck'),
    path('hello/', hello, name='hello'),
    path('index/', index, name='index')
]
