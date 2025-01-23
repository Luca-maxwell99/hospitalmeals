from django.contrib import admin
from django.urls import path, include
from users import views as users_views

urlpatterns = [
    path('select/', include('meal_selection.urls')),
    path('', include('allauth.urls')),  # Trailing slash
    path('list/', include('meals.urls')),  # Trailing slash
    path('home/', users_views.home, name='home'),
    path('admin/', admin.site.urls),
]
