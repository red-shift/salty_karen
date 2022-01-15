from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.crypto import get_random_string
from django.utils.text import slugify

from .models import KarenPost


@receiver(pre_save, sender=KarenPost)
def add_slug_to_post(sender, instance, *args, **kwargs):
    if instance and not instance.slug:
        slug = slugify(instance.title)
        random_string = get_random_string(length=8)
        instance.slug = slug + '-' + random_string
