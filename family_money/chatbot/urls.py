from django.urls import path
from .views import get_chatbot_response_view

app_name = 'chatbot'

urlpatterns = [
    path('get_chatbot_response/', get_chatbot_response_view, name='get_chatbot_response'),
]