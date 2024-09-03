from django.db import models
from django.contrib.auth.models import User

class EmailNotification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Email to {self.user.username} at {self.sent_at}'

class NotificationPreference(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    weekly_digest = models.BooleanField(default=True)
    bill_reminders = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.user.username} Preferences'