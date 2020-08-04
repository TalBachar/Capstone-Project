import os
from django.db.models.signals import pre_save, post_save, post_delete
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Pet


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Pet.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.pet.save()
