
from django.urls import path, include
from users import views

app_name = 'users'

urlpatterns = [
    path('orders/<int:itemid>/<int:pdcd>/<str:user>/',views.Orders,name='orders'),
    path('updateorder/<int:orderid>/<int:itemid>/',views.update_orders,name='updateorder'),
    path('cart/', views.view_cart,name='cart'),
    path('addtocart/<int:itemid>/',views.add_to_cart,name='addtocart'),
    path('removecart/<int:itemid>/',views.remove_to_cart,name='remove_cart'),
    
]