from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


# Create your models here.
class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('profile', args=[self.username])
