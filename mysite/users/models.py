from django.db import models
from django.contrib.auth.models import User
from ecom.models import Item
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User,max_length=100, on_delete=models.CASCADE)
    location = models.CharField(max_length=200)
    image = models.ImageField(upload_to='profile_pictures',default='profilepic.jpg')
    user_type = models.CharField(default='user_type')
    
    
    def __str__(self):
        return self.user.username
    
    
class ItemPictures(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='item_pictures', default='yooo.jpg')
    
    def __str__(self):
        return self.name
    
    
class CusOrders(models.Model):
    order_id = models.AutoField(primary_key=True)
    prod_code = models.IntegerField()
    quantity = models.IntegerField(default=1)
    username = models.CharField(max_length=100)
    
    
    def __str__(self):
        return str(
            (
                self.order_id,
                self.prod_code,
                self.quantity,
                self.username
            )
        )
        
class CartItem(models.Model):
    product = models.ForeignKey(Item, on_delete=models.CASCADE,default=7)
    quantity = models.PositiveIntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='kind')
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.quantity} x {self.product.item_name}"
    
    

class CustomerRatingFeedback(models.Model):
    prod_code = models.IntegerField(defaukt=1)
    ratings = models.FloatField(default=0.0)
    feedback = models.TextField()
    username = models.CharField(max_length=255)
    
    
    def __str__(self):
        return self.username