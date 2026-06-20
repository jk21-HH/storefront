from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

class Tag(models.Model):
    label = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)

class TaggedItem(models.Model):
    #  What tag is applied to what object
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    # Type of the object that is tagged (product, video, article, etc.)
    # ID of the object that is tagged
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()