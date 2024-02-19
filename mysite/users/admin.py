from django.contrib import admin
from users.models import Profile, ItemPictures,CusOrders, CartItem, CustomerRatingFeedback
# Register your models here.

class UserIndexView(admin.ModelAdmin):
    list_display = ['user','location','user_type']


admin.site.register(Profile, UserIndexView)
admin.site.register(ItemPictures)
admin.site.register(CusOrders)
admin.site.register(CartItem)
admin.site.register(CustomerRatingFeedback)

