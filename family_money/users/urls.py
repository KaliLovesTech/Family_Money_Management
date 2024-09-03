from django.urls import path
from . import views

app_name = 'users'  # This registers the namespace 'users'

urlpatterns = [
    path('profile/', views.profile_view, name='profile'),
    path('change-password/', views.change_password, name='change_password'),
    path('onboarding/', views.onboarding_view, name='onboarding'),
]