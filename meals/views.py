from django.shortcuts import render
from django.http import HttpResponse

def meal_view(request):
    return HttpResponse("This view will handle meal options including CRUD functionallity as well as store meal details such as name, ingredients etc")
