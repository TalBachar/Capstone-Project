from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils.text import slugify
from django.utils.timezone import now

from accounts.models import User



class Pet(models.Model):
    title = models.CharField(max_length=200)
    #name = models.CharField(max_length=128)
    #api_id = models.CharField(max_length=128)
    #pet_id = models.CharField(max_length=128)
    #animal_type = models.CharField(max_length=128)
    #breed = models.CharField(max_length=128)
    #color = models.CharField(max_length=96)
    #gender = models.CharField(max_length=128)
    #age = models.CharField(max_length=128)
    #size = models.CharField(max_length=128)
    #zipcode = models.CharField(max_length=128, null = False)
    #photo_url = models.CharField(max_length=128)


def __str__(self):
    return self.title

def save(self, *args, **kwargs):
    self.slug = slugify(self.title)
    super(Pet, self).save(*args, **kwargs)
