from django.urls import path, include
from ecom import views

app_name = 'ecom'

urlpatterns = [
    path('BrowseAllProduct',views.default,name="Allproducts"),
    path('home/',views.index,name='index'),
    path('detail/<int:item_id>/',views.details,name="detail"),
    path('createitem/',views.create_item,name="createitem"),
    path('update/<int:item_id>/',views.update_item,name="updateitem"),
    path('delete/<int:item_id>/', views.delete_item, name='deleteitem')
]

