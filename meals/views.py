from django.shortcuts import render
from django.views import View
from .models import Meal

class MealListView(View):
    def get(self, request):
        mains = Meal.objects.filter(is_main=True)  # Get all main meals
        sides = Meal.objects.filter(is_side=True)  # Get all side meals
        return render(request, 'meals/meal_list.html', {'mains': mains, 'sides': sides})


def home(request):
    return render(request, 'meals/home.html')
