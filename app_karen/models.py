import uuid as uuid_lib

from django.conf import settings
from django.db import models
from django.urls import reverse

from core.models import TimeStampedModel


# Create your models here.
class KarenPost(TimeStampedModel):
    IS_APPROVED_CHOICES = (
        (False, "No"),
        (True, "Yes"),
    )
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=255, unique=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='karen_posts')
    name = models.CharField(max_length=64)
    location = models.CharField(max_length=64)
    description = models.TextField()
    video = models.FileField(null=True, blank=True)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'slug': self.slug})


class Comment(TimeStampedModel):
    uuid = models.UUIDField(default=uuid_lib.uuid4, editable=False)
    post = models.ForeignKey(KarenPost, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.CharField(max_length=240)

    def __str__(self):
        return self.content

    def count(self):
        return self.post.comments.count()


