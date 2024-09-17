from django.urls import path
from common.views import dashboard_view # Import other necessary views

app_name = 'common'

urlpatterns = [
    path('dashboard/', dashboard_view, name='dashboard'),
]