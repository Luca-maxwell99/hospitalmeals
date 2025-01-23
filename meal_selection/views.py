from django.shortcuts import render, redirect, HttpResponse
from .forms import MealSelectionForm
from .models import MealSelection


def meal_selection_view(request):
    if request.method == 'POST':
        form = MealSelectionForm(request.POST)
        if form.is_valid():
            meal_selection = form.save(commit=False)
            meal_selection.user = request.user  # Set the user manually
            meal_selection.save()
            return HttpResponse("Success") # Redirect after successful form submission
    else:
        form = MealSelectionForm()
    return render(request, 'meal_selection/meal_selection_form.html', {'form': form})
