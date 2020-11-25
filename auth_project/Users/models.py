from django.db import models
AUTH_USER_MODEL = 'Users.CustomUser'
AUTH_USER_MODEL = 'Users.CustomUser'

from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    pass