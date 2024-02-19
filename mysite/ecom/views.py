from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Item, Category, History
from ecom.forms import ItemForm
from django.contrib import messages
from users.models import CusOrders,CustomerRatingFeedback
from django.contrib.auth.decorators import login_required



# Create your views here.\\
    
def default(request):
    items_list = Item.objects.all()
    
    context = {
        'items_list':items_list
    }
    return render (request,"ecom/homepage.html", context)

def index(request):
    
    categories = Category.get_all_category()
    categoryID = request.GET.get('category')
    
    if categoryID:
        Itemlist = Item.get_all_product_by_categoryID(categoryID)
    else:
        Itemlist = Item.get_all_item()
    
    
    
    context = {
        'Itemlist':Itemlist,
        'categories':categories
    }
    
    return render (request, 'ecom/index.html', context)

@login_required
def details(request,item_id):
    
    item = Item.objects.get(id=item_id)
    items = Item.objects.all()[:4]
    hist = History.objects.filter(
        prod_code = item.prod_code
    )
    
    
    crf = CustomerRatingFeedback.objects.filter(
        prod_code = item.prod_code
    )
    
    if request.user.profile.user_type == 'saler' or request.user.profile.user_type == 'admin':
        oco = CusOrders.objects.filter(
            prod_code = item.prod_code
        )
    
    if request.user.profile.user_type == 'cust':
        oco = CusOrders.objects.filter(
            prod_code = item.prod_code,
            username = request.user.username 
        )
    
    context = {
        'item':item,
        'oco':oco,
        'hist':hist,
        'items':items,
        'crf':crf,
        
    }
    return render (request, 'ecom/detail.html', context)
@login_required
def create_item(request):
    form = ItemForm(request.POST or None)
    
    if form.is_valid():
        if form.cleaned_data['item_price'] <= 0:
            messages.error(request, "Item price cannot be zero or less than zero")
            return redirect("ecom:createitem")
        else:
            form.save()
            objhist = History(
                username = request.user.username,
                prod_code = request.POST['prod_code'],
                item_name = request.POST.get('item_name'),
                operation_type = 'created',
                user_type = request.user.profile.user_type
            )
            objhist.save()
            return redirect('ecom:index')
    context = {
        'form':form
    }
    return render (request,"ecom/item-form.html", context)
@login_required
def update_item(request,item_id):
    item = Item.objects.get(id=item_id)
    form = ItemForm(request.POST or None, instance=item)
    if request.method == 'POST':
        if form.is_valid():
            if form.cleaned_data['item_price'] <= 0:
                messages.error(request, "Item price cannot be zero or less than zero")
                return redirect("ecom:updateitem")
            else:
                form.save()
                objhist = History(
                username = request.user.username,
                prod_code = request.POST['prod_code'],
                item_name = request.POST.get('item_name'),
                operation_type = 'updated',
                user_type = request.user.profile.user_type
            )
                objhist.save()
                return redirect ('ecom:detail',item_id)
        
    context = {
        'form':form
    }
        
    return render (request, 'ecom/item-form.html', context)
@login_required
def delete_item(request, item_id):
    item = Item.objects.get(id=item_id)
    if request.method == 'POST':
        objhist = History(
                username = request.user.username,
                prod_code = item.prod_code,
                item_name = item.item_name,
                operation_type = 'delete',
                user_type = request.user.profile.user_type
            )
        objhist.save()
        item.delete()
        return redirect ('ecom:index')
    
    context = {
        'item':item
    }
    return render(request, 'ecom/item-delete.html', context)