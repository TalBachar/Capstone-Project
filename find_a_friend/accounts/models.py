import os
from django.db import models
from django.contrib.auth.models import User


class Pet(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    pet_type = models.CharField(max_length=100, null=True, blank=True)
    pet_age = models.CharField(max_length=150, null=True, blank=True)
    pet_breed = models.CharField(max_length=150, null=True, blank=True)

    def __str__(self):
        return f'{self.user.username} Pet'
