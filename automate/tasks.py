from celery import shared_task
import time
from celery.schedules import crontab
from .models import Product

@shared_task
def my_background_task():
    print("yo")
    a=0
    te=Product.objects.all()
    print(te)
   
    
    return a
