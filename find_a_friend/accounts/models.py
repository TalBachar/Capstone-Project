from django.db import models
from accounts.managers import UserManager
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass
    # email = models.EmailField(unique=True, blank=False,
    #                           error_messages={
    #                               'unique': "Email already exists.",
    #                           })
    #
    # USERNAME_FIELD = "email"
    # REQUIRED_FIELDS = []
    #
    # def __str__(self):
    #     return self.email
    #
    # def get_full_name(self):
    #     return self.email
    #
    # def get_short_name(self):
    #     return self.email
    #
    # objects = UserManager()
