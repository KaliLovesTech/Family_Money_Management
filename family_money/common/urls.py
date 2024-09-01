from django.urls import path
from . import views

app_name = 'common'  # Set the app name for namespacing

urlpatterns = [
    # Example route: a shared dashboard or user profile
    path('dashboard/', views.dashboard, name='dashboard'),
    path('profile/', views.profile, name='profile'),
    # Add more common routes as needed
]
