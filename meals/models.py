from django.db import models

# Create your models here.
class Meal(models.Model):
    
    name = models.CharField(max_length=100)
    ingredients = models.TextField()
    allergens = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    is_main = models.BooleanField(default=False)
    is_side = models.BooleanField(default=False)
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.name

