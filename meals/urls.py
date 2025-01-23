from django.urls import path
from . import views

urlpatterns = [
    path('', views.meal_view, name='meal_list'),
]
