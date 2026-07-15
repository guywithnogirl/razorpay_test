from django.shortcuts import render
from django.http import JsonResponse

def hello_api(request):
    return JsonResponse({'message': 'Hello, World!'})

def home(request):
    return render(request, 'home.html')