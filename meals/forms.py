from django import forms
from .models import Main, Side

class MainForm(forms.ModelForm):
    class Meta:
        model = Main
        fields = ['name', 'ingredients', 'allergens']

class SideForm(forms.ModelForm):
    class Meta:
        model = Side
        fields = ['name', 'ingredients', 'allergens']
