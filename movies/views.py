from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view

# Create your views here.

@api_view(http_method_names=["GET"])
def movie_list(request):
    data = {
        "message": "OK"
    }
    return JsonResponse(data=data)