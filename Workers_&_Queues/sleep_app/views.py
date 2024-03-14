from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from time import sleep

def slow_view(request):
    data = {
        "name": "Eunice Atieno"
    }
    sleep(7)
    return JsonResponse(data)