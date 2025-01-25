from django.urls import path
from . import views

urlpatterns = [
     path('', views.home, name='home'),
    path('meals/', views.MealListView.as_view(), name='meal-list'),
]



   
