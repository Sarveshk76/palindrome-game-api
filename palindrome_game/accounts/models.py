from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(max_length=500, blank=True)
    mobile_no = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return self.user.username