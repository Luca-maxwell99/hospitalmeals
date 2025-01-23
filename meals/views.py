from django.shortcuts import render
from .models import Meal

def meal_view(request):
    meals = Meal.objects.all()  # Retrieve all Meal objects
    return render(request, 'meals/meal_list.html', {'object_list': meals})
