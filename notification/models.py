from django.conf import settings
#from django.contrib.auth.models import User
from django.db import models

class Notification(models.Model):
    MESSAGE = 'message'
    APPLICATION = 'application'

    CHOICES = (
        (MESSAGE, 'Message'),
        
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='notifications', on_delete=models.CASCADE)
    notification_type = models.CharField(max_length=20, choices=CHOICES)
    is_read = models.BooleanField(default=False)
    extra_id = models.IntegerField(null=True, blank=True)
    message = models.TextField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='creatednotifications', on_delete=models.CASCADE)

    class Meta:
        ordering = ['-created_at']