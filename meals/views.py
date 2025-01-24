from django.shortcuts import render, HttpResponse
from .models import Meal

def meal_view(request):
    meals = Meal.objects.all()  # Retrieve all Meal objects, change to 'filter(author=1)' if you want to filter by author
    context = {
        'object_list': meals,
        'title': 'Available Meals'
    }
    return render(request, 'meals/meal_list.html', context)

def home(request):
    return render(request, 'meals/home.html')
