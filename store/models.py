from django.db import models

# Create your models here.

class Promotion(models.Model):
    description = models.CharField(max_length=255)
    discount = models.FloatField()
    # product_set = models.ManyToManyField('Product') #ManyToManyField means that each Promotion can be associated with many Products, and each Product can be associated with many Promotions
class Collection(models.Model):
    title = models.CharField(max_length=255)
    featured_product = models.ForeignKey('Product', on_delete=models.SET_NULL, null=True, related_name='+') 
    #ForeignKey means that each Collection can only be associated with one Product, but each Product can be associated with many Collections. 
    #on_delete=models.SET_NULL means that if the Product is deleted, the featured_product field for all Collections will be set to NULL. related_name='+' means that the reverse relationship will not be created. 
    #This is useful to avoid name collisions for fields with the same name. 
    #the '+' is a special value that can only be used in this context. It means that the reverse relationship for this field will be disabled.

class Product(models.Model):
    #sku = models.CharField(max_length=10,primary_key=True, unique=True) #unique=True means that no two products can have the same SKU
    title = models.CharField(max_length=255) 
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()
    inventory = models.IntegerField()
    last_updated = models.DateTimeField(auto_now=True) #different from auto_now_add which is only when created
    collection = models.ForeignKey(Collection, on_delete=models.PROTECT) #ForeignKey means that each Product can only be associated with one Collection, but each Collection can be associated with many Products
    promotions = models.ManyToManyField(Promotion) #ManyToManyField means that each Product can be associated with many Promotions, and each Promotion can be associated with many Products

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
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT) #ForeignKey means that each Order can only be associated with one Customer, but each Customer can be associated with many Orders


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT) #ForeignKey means that each OrderItem can only be associated with one Order, but each Order can be associated with many OrderItems
    product = models.ForeignKey(Product, on_delete=models.PROTECT) #ForeignKey means that each OrderItem can only be associated with one Product, but each Product can be associated with many OrderItems
    quantity = models.PositiveSmallIntegerField() #PositiveSmallIntegerField means that the value must be a positive integer
    unit_price = models.DecimalField(max_digits=6, decimal_places=2) #max_digits=6 means that the value can have up to 6 digits, and decimal_places=2 means that 2 of those digits can be after the decimal point


class Address(models.Model):
    street = models.CharField(max_length=255) 
    city = models.CharField(max_length=255) 
    #zip = models.CharField(max_length=255)
    #customer = models.OneToOneField(Customer, on_delete=models.CASCADE, primary_key=True) #OneToOneField means that each Address can only be associated with one Customer, and each Customer can only have one Address
    #option2:
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE) #ForeignKey means that each Address can be associated with many Customers, but each Customer can only have one Address
    

class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    checked_out_at = models.DateTimeField(null=True)
    #customer = models.OneToOneField(Customer, on_delete=models.CASCADE, primary_key=True) #OneToOneField means that each Cart can only be associated with one Customer, and each Customer can only have one Cart
    #option2:
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE) #ForeignKey means that each Cart can be associated with many Customers, but each Customer can only have one Cart


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE) #ForeignKey means that each CartItem can only be associated with one Cart, but each Cart can be associated with many CartItems
    product = models.ForeignKey(Product, on_delete=models.CASCADE) #ForeignKey means that each CartItem can only be associated with one Product, but each Product can be associated with many CartItems
    quantity = models.PositiveSmallIntegerField() #PositiveSmallIntegerField means that the value must be a positive integer
    