from django.urls import path
from . import views

urlpatterns = [
    path('select/', views.meal_selection_view, name='meal_selection'),
    path('meals_list/', views.meal_selection_list_view, name='meal_selection_list'),
]
