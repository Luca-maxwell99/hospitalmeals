from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.meal_view, name='meal_list'),
    path('', views.home, name='home')
]
