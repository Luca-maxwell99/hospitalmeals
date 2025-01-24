from django.shortcuts import render, redirect, HttpResponse, reverse
from .forms import MealSelectionForm
from .models import MealSelection


from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import MealSelectionForm

def meal_selection_view(request):
    if request.method == 'POST':
        form = MealSelectionForm(request.POST)
        if form.is_valid():
            meal_selection = form.save(commit=False)
            meal_selection.user = request.user  # Set the user manually
            meal_selection.save()
            return redirect(reverse('meal_selection_list'))  # Redirect after successful form submission
    else:
        form = MealSelectionForm()

    context = {
        'form': form,
        'title': 'Meal Selection'
    }
    return render(request, 'meal_selection/meal_selection_form.html', context)


def meal_selection_list_view(request):

    user = request.user

    meal_selections = MealSelection.objects.filter(user=user)

    str = ""

    for meal in meal_selections:
        str += meal.meal.name

    print(str)

    return HttpResponse(str)


def edit_meal_selection_view(request, id):
    meal_selection = MealSelection.objects.filter(id=id).first()

    if request.method == 'POST':
        form = MealSelectionForm(request.POST)
        if form.is_valid():
            meal_selection = form.save(commit=False)
            meal_selection.user = request.user  # Set the user manually
            meal_selection.save()
            return redirect(reverse('meal_selection_list'))# Redirect after successful form submission
    else:
        form = MealSelectionForm()
    return render(request, 'meal_selection/meal_selection_form.html', {'form': form})