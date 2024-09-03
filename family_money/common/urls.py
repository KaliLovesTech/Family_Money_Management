from django.urls import path
from users.views import profile_view, change_password  # Import views directly from users
from common.views import dashboard_view  # Import other necessary views

app_name = 'common'

urlpatterns = [
    path('profile/', profile_view, name='profile'),
    path('profile/change-password/', change_password, name='change_password'),
    path('dashboard/', dashboard_view, name='dashboard'),
]