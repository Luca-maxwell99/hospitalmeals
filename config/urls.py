from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include('meal_selection.urls')),
    path('accounts/', include('allauth.urls')),
    path('', include('meals.urls')),  # Trailing slash
    path('admin/', admin.site.urls),
]
