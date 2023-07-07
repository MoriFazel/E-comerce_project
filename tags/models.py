from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

# Create your models here.
#what is a tag? a tag is a label that we can attach to a product
#what tag is attached to what product? we need a many to many relationship
class Tag(models.Model):
    label = models.CharField(max_length=255)

    
class TaggedItem(models.Model):
    #what tag is attached to what product?
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    #type of product
    #ID of product
    product = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    #content_object = GenericForeignKey()