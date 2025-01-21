from django import forms
from .models import MealSelection

class MealSelectionForm(forms.ModelForm):
    class Meta:
        model = MealSelection
        fields = ['meal', 'meal_type', 'confirmed']
