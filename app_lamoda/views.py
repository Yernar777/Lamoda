from django.shortcuts import render
from .models import *
from .forms import *
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import auth
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
def lamoda(request):
    products = LamodaCategory.objects.all()
    categoryes = Category.objects.all()
    shapkyes = LamodaShapka.objects.all()
    shapkyes1 = LamodaShapka1.objects.all()
    return render(request,'index_lamoda.html',{'categoryes':categoryes,'shapkyes':shapkyes,'shapkyes1':shapkyes1,'products':products,})

def lamoda_category(request, id):
    product = LamodaCategory.objects.filter(category_id=id)
    return render(request, 'lamoda_category.html',{'product':product})


def review_functional(request):
    form1 = ReviewForms1()
    if request.method == 'POST':
        form1 = ReviewForms1(request.POST)
        if form1.is_valid():
            form1.save()
            return redirect('succes')
    else:
        form = ReviewForms()
    return render(request, 'forms.html',{'form': form, 'form1': form1,})





@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(LamodaCategory, id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, item_created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not item_created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('cart_detail')

@login_required
def cart_detail(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    total_price = sum(item.get_total_price() for item in cart.items.all())
    return render(request, 'cart_detail.html', {'cart': cart, 'total_price': total_price})

@login_required
def increase_quantity(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id)
    cart_item.quantity += 1
    cart_item.save()
    return redirect('cart_detail')

@login_required
def decrease_quantity(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()  
    return redirect('cart_detail')

@login_required
def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id)
    cart_item.delete()  
    return redirect('cart_detail')
