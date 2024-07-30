from django.contrib.contenttypes.fields import GenericForeignKey
from django.db import models
from django.contrib.contenttypes.models import ContentType
from apps.users.models import User


class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    message = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)

    def __str__(self):
        return f'Notification for {self.user} - {self.message}'
