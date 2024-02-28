from django.http import JsonResponse
from .tasks import my_background_task
from django.shortcuts import render
import time

def automate_view(request):
    # Create a dictionary with your data
    data = {
        'key1': 'value1',
        'key2': 'value2',
    }
    number = 5  # Replace with the actual number you want to square
    
    result = my_background_task.delay()
    

    # Include the result in the response
   
    # Return a JsonResponse with the data
    return JsonResponse(data)
