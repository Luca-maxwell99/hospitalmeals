from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import MealSelection
from django.contrib.auth.mixins import LoginRequiredMixin

class UserMealSelectionListView(LoginRequiredMixin, ListView):
    model = MealSelection
    template_name = 'meal_selection/user_meal_selection_list.html'

    def get_queryset(self):
        return MealSelection.objects.filter(user=self.request.user)

class MealSelectionDetailView(LoginRequiredMixin, DetailView):
    model = MealSelection
    template_name = 'meal_selection/meal_selection_detail.html'

class MealSelectionCreateView(LoginRequiredMixin, CreateView):
    model = MealSelection
    fields = ['meal', 'meal_type', 'confirmed']
    template_name = 'meal_selection/meal_selection_form.html'
    success_url = reverse_lazy('user_meal_selection_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class MealSelectionUpdateView(LoginRequiredMixin, UpdateView):
    model = MealSelection
    fields = ['meal', 'meal_type', 'confirmed']
    template_name = 'meal_selection/meal_selection_form.html'
    success_url = reverse_lazy('user_meal_selection_list')

class MealSelectionDeleteView(LoginRequiredMixin, DeleteView):
    model = MealSelection
    template_name = 'meal_selection/meal_selection_confirm_delete.html'
    success_url = reverse_lazy('user_meal_selection_list')
