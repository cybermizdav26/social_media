from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Follow(models.Model):
    following = models.ForeignKey(User, related_name="following", on_delete=models.CASCADE)
    follower = models.ForeignKey(User, related_name="followers", on_delete=models.CASCADE)
    is_following = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.following.username} -> {self.follower.username}'

