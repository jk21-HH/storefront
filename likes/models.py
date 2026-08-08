from django.conf import settings
from django.db import models

from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

class LikeItem(models.Model):
    #  What user's like is applied to what object
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # Type of the object that is liked (product, video, article, etc.)
    # ID of the object that is liked
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()