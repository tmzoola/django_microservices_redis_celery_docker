import time
from celery import shared_task


@shared_task
def debug_task():
    print('Hello Debug Task!')


@shared_task
def periodic_task():
    print('Periodic task executed!')
