from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=255) 
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()
    inventory = models.IntegerField()
    last_updated = models.DateTimeField(auto_now=True) #different from auto_now_add which is only when created

class Customer(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True) #unique=True means that no two customers can have the same email address
    phone = models.CharField(max_length=255)
    birth_date = models.DateField(null=True) #null=True means that the birth_date field can be empty
    #created_at = models.DateTimeField(auto_now_add=True) #auto_now_add=True means that the created_at field will be set to the current date and time when a Customer is created