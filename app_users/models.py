from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser


# Always extend the user model so you can add new fields, methods as needed
class CustomUser(AbstractUser):
    birthdate = models.DateField(null=True)


class TermsOfService(models.Model):
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=False)


class UserTermsOfService(models.Model):
    tos = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='tos')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)
