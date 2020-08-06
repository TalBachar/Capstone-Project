from django.db import models
from django.contrib.auth.models import User

class Fav(models.Model):
	fav_name= models.CharField(max_length=128, blank=True, default='')
	fav_age= models.CharField(max_length=128, blank=True, default='')
	fav_breed= models.CharField(max_length=128, blank=True, default='')
	fav_url = models.TextField(max_length=128, blank=True, default='')
	fav_image = models.TextField(max_length=128, blank=True, default='')
	user_key = models.ForeignKey(User, on_delete=models.CASCADE)
