from django.urls import path
from .views import send_upcoming_bills_email_view, send_weekly_digest_email_view

app_name = 'notifications'

urlpatterns = [
    path('send_upcoming_bills_email/', send_upcoming_bills_email_view, name='send_upcoming_bills_email'),
    path('send_weekly_digest_email/', send_weekly_digest_email_view, name='send_weekly_digest_email'),
]