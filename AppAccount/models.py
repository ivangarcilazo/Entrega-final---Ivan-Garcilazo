from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

class CarPosts(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title=models.CharField(max_length=40)
    price=models.IntegerField()
    image = models.ImageField(upload_to='images/')
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
    