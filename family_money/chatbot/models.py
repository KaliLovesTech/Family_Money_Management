from django.db import models
from django.contrib.auth.models import User

class ChatbotQuery(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    query = models.TextField()
    response = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Query by {self.user.username} on {self.timestamp}'