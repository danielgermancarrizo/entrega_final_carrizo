from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Message(models.Model):
    title = models.CharField(max_length=1000, null=True)
    content = models.TextField(null=True)
    created = models.DateTimeField(auto_now_add=True)
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender', null=True)
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receiver', null=True)
   

    class Meta:
        ordering = ['created']

