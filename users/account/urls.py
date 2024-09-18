from django.urls import path
from account.views import healthcheck


urlpatterns = [
    path('healthcheck/', healthcheck, name='healthcheck')
]