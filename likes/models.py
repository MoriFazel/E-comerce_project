from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
# Create your models here.

class LikedItem(models.Model):
    #who liked what?
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #what did they like?
    #type of product
    #ID of product
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    #product = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    content_object = GenericForeignKey()
    
    #def __str__(self):
    #    return f"{self.user.username} likes {self.content_object}"