from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    catg_name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.catg_name
    
    @staticmethod
    def get_all_category():
        return Category.objects.all()
    



class Item(models.Model):
    category = models.ForeignKey(Category, default=1 ,on_delete=models.CASCADE)
    prod_code = models.IntegerField(default=50)
    added_by = models.CharField(max_length=100, default='user_name')
    saler_name = models.ForeignKey(User, on_delete=models.CASCADE, default=3)
    item_name = models.CharField(max_length=100)
    item_desc = models.CharField(max_length=500,default="There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humour, or randomised words which don't look even slightly believable. If you are going to use ")
    item_price = models.PositiveIntegerField(default=1)
    item_image = models.CharField(max_length=500)
    
    
    def __str__(self):
        return self.item_name
    
    @staticmethod
    def get_all_item():
        return Item.objects.all()
    
    @staticmethod
    def get_all_product_by_categoryID(category_id):
        if category_id:
            return Item.objects.filter(category_id=category_id)
        else:
            return Item.get_all_item()
    

    
class History(models.Model):
    username = models.CharField(max_length=100)
    prod_code = models.IntegerField()
    item_name = models.CharField(max_length=100)
    operation_type = models.CharField(max_length=100)
    user_type = models.CharField(max_length=100)
    
    
    def __str__(self):
        return self.request.user.username
