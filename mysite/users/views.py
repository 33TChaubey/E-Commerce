from django.shortcuts import render, redirect
from users.models import Profile, CusOrders, CartItem
from users.forms import ProfformEdit, ProfformCreate, UpdateOrder
from ecom.models import Item
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def ProfilePage(request):
    prof = Profile.objects.get(user=request.user.id)
    context = {
        'prof':prof
    }
    return render(request,'users/profilepage.html',context)

@login_required
def ProfileEdit(request,prof_id):
    prof = Profile.objects.get(id=prof_id)
    form = ProfformEdit(request.POST or None, request.FILES or None, instance=prof)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect ("profilepage")
    context = {
        'form':form
    }
    
    return render (request, "users/profformedit.html", context)
@login_required
def ProfileCreate(request, user_id):
    prof = Profile.objects.get(user=user_id)
    profform = ProfformCreate(request.POST or None, request.FILES or None,instance=prof)
    if profform.is_valid():
        profform.save()
        return render ("ecom:index")
    context = {
        'prof':prof,
        'profform':profform
    }
    
    return render(request,"users/profformcreate.html",context)

@login_required
def Orders(request, itemid,pdcd,user):
    
    if request.method == 'POST':
        quantity = request.POST['qty']

        cusordobj = CusOrders(
            prod_code = pdcd,
            quantity = quantity,
            username = user
        )
        
        cusordobj.save()
        return redirect('ecom:detail', item_id=itemid)
    
    context = {
        'username':user,
        'pdcd':pdcd
            
    }
    return render (request, "users/orders.html", context)
@login_required
def update_orders(request,orderid,itemid):
    coo = CusOrders.objects.get(order_id=orderid)
    form = UpdateOrder(request.POST or None, instance=coo)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect ('ecom:detail', item_id=itemid)
    
    context = {
        'form':form
    }
    return render (request, 'users/updateorder.html', context)
@login_required
def view_cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total_price = sum(item.product.item_price * item.quantity for item in cart_items)
    
    
    context = {
        'cart_items':cart_items,
        'total_price':total_price
    }
    return render (request, 'users/cart.html', context)

@login_required
def add_to_cart(request, itemid):
    product = Item.objects.get(id=itemid)
    cart_item, created = CartItem.objects.get_or_create(product=product,user=request.user)
    
    cart_item.quantity += 1
    cart_item.save()
    return redirect ('users:cart')

@login_required
def remove_to_cart(request,itemid):
    cart_item = CartItem.objects.get(id=itemid)
    cart_item.delete()
    return redirect ('users:cart')

from django.shortcuts import render
from django.http import HttpResponse


from django.urls import path
from . import views

