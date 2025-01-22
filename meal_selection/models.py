from django.db import models
from meals.models import Meal
from django.contrib.auth import get_user_model

User = get_user_model()

class MealSelection(models.Model):
    MEAL_TYPE_CHOICES = [
        ('lunch', 'Lunch'),
        ('dinner', 'Dinner'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    date_selected = models.DateTimeField(auto_now_add=True)
    meal_type = models.CharField(max_length=100, choices=MEAL_TYPE_CHOICES, default='lunch')
    confirmed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user} selected {self.meal} on {self.date_selected}"
