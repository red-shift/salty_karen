from django.db import models


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Use abstract true to allow a model to inhere similar properties without creating database tables
    class Meta:
        abstract = True