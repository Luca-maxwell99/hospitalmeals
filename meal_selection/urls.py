from django.urls import path
from . import views

urlpatterns = [
    path('', views.UserMealSelectionListView.as_view(), name='user_meal_selection_list'),
    path('create/', views.MealSelectionCreateView.as_view(), name='meal_selection_create'),
    path('<int:pk>/', views.MealSelectionDetailView.as_view(), name='meal_selection_detail'),
    path('<int:pk>/update/', views.MealSelectionUpdateView.as_view(), name='meal_selection_update'),
    path('<int:pk>/delete/', views.MealSelectionDeleteView.as_view(), name='meal_selection_delete'),
]
