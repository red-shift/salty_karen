from django.db import models
from django.contrib.auth.models import AbstractUser


# Always extend the user model so you can add new fields, methods as needed
class CustomUser(AbstractUser):
    birthdate = models.DateField()
