from django.shortcuts import render, redirect
from .forms import MealSelectionForm
from .models import MealSelection
from django.contrib.auth.decorators import login_required

@login_required
def meal_selection_view(request):
    if request.method == 'POST':
        form = MealSelectionForm(request.POST)
        if form.is_valid():
            meal_selection = form.save(commit=False)
            meal_selection.user = request.user  # Set the user manually
            meal_selection.save()
            return redirect('meal_selection_success')  # Redirect after successful form submission
    else:
        form = MealSelectionForm()
    return render(request, 'meal_selection/meal_selection_form.html', {'form': form})
