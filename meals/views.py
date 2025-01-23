from django.shortcuts import render
from .models import Meal

def meal_view(request):
    meals = Meal.objects.all()  # Retrieve all Meal objects, change to 'filter(author=1)' every user is assigned a PK, this would be the first user. 
    return render(request, 'meals/meal_list.html', {'object_list': meals})
