from django.db import models

# Create your models here.
class Product(models.Model):
    #sku = models.CharField(max_length=10,primary_key=True, unique=True) #unique=True means that no two products can have the same SKU
    title = models.CharField(max_length=255) 
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()
    inventory = models.IntegerField()
    last_updated = models.DateTimeField(auto_now=True) #different from auto_now_add which is only when created
    
class Customer(models.Model):
    MEMBERSHIP_BRONZE = 'B'
    MEMBERSHIP_SILVER = 'S'
    MEMBERSHIP_GOLD = 'G'

    MEMBERSHIP_CHOICES = [
        (MEMBERSHIP_BRONZE, 'Bronze'),
        (MEMBERSHIP_SILVER, 'Silver'),
        (MEMBERSHIP_GOLD, 'Gold'),
    ]
    

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True) #unique=True means that no two customers can have the same email address
    phone = models.CharField(max_length=255)
    birth_date = models.DateField(null=True) #null=True means that the birth_date field can be empty
    #created_at = models.DateTimeField(auto_now_add=True) #auto_now_add=True means that the created_at field will be set to the current date and time when a Customer is created
    membership = models.CharField(max_length=50, choices=MEMBERSHIP_CHOICES, default= MEMBERSHIP_BRONZE)


class Order(models.Model):
    PAYMENT_STATUS_PENDING = 'P'
    PAYMENT_STATUS_COMPLETE = 'C'
    PAYMENT_STATUS_FAILED = 'F'

    PAYMENT_STATUS_CHOICES = [
        (PAYMENT_STATUS_PENDING, 'Pending'),
        (PAYMENT_STATUS_COMPLETE, 'Complete'),
        (PAYMENT_STATUS_FAILED, 'Failed'),
    
    ]
    placed_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(max_length=50, choices=PAYMENT_STATUS_CHOICES, default= PAYMENT_STATUS_PENDING)


class Address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    #zip = models.CharField(max_length=255)
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE, primary_key=True) #OneToOneField means that each Address can only be associated with one Customer, and each Customer can only have one Address