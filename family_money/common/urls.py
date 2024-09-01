from django.urls import path
from . import views

app_name = 'common'

urlpatterns = [
    # profile
    path('profile/', views.profile_view, name='profile'),
    path('profile/change-password/', views.change_password, name='change_password'),
    # dashboard 
    path('dashboard/', views.dashboard_view, name='dashboard'),
]