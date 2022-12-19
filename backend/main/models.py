from django.db import models
from django.utils import timezone
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=20)
    # storeID = models.IntegerField()
    created_at = models.DateTimeField(default=timezone.now )
    def __str__(self):
        return self.name
    
class Menu(models.Model):
    # storeID = models.IntegerField()
    # consumerID = models.IntegerField()
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    image =models.TextField(max_length=50)
    info = models.TextField()
    stock = models.BooleanField(null=True)
    like = models.IntegerField(null=True)
    created_at = models.DateTimeField(default=timezone.now)
    category = models.OneToOneField(Category, related_name="Category", on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return self.name
    
    
class Event(models.Model):
    name = models.TextField()
    data = models.TextField()
    image = models.TextField()
    # storeID = models.IntegerField()
    created_at = models.DateTimeField(default=timezone.now )
    def __str__(self):
        return self.name
class Carosel(models.Model):
    data = models.TextField()
    image = models.TextField()
    # storeID = models.IntegerField()
    created_at = models.DateTimeField(default=timezone.now )

class Home(models.Model):
    # storeID = models.IntegerField()
    event = models.ForeignKey(Event, related_name="Event", on_delete=models.SET_NULL, null=True)
    carosel = models.ForeignKey(Carosel, related_name="Carosel", on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(default=timezone.now )
    
class Order(models.Model):
    # storeID = models.IntegerField()
    # consumerID = models.IntegerField()
    menu = models.ManyToManyField(Menu, related_name="Menu")
    price = models.IntegerField(null=True)
    memo = models.TextField()
    made = models.BooleanField()
    pickup = models.BooleanField()
    created_at = models.DateTimeField(default=timezone.now )
    
class Coupon(models.Model):
    # storeID = models.IntegerField()
    # consumerID = models.IntegerField()
    stamp = models.IntegerField()
    created_at = models.DateTimeField(default=timezone.now )