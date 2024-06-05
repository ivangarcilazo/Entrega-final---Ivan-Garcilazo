from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from AppAccount.models import *

class CommentPost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(CarPosts, on_delete=models.CASCADE, default=1)
    comment = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'Comentario de: {self.user.name}'
    