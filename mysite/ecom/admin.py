from django.contrib import admin
from ecom.models import Item, Category, History

# Register your models here.

class ItemView(admin.ModelAdmin):
    list_display = ['item_name','item_price']


admin.site.register(Item,ItemView)
admin.site.register(Category)
admin.site.register(History)

