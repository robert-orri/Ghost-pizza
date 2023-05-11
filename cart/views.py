from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Cart, CartItems
from ghost.models import Pizza
from django import template

# Create your views here.
def index(request):
    return render(request, 'cart/index.html')


@login_required
def add_to_cart(request, pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItems.objects.get_or_create(cart=cart, pizza=pizza)
    cart_item.quantity += 1
    cart_item.save()
    return redirect('cart')


@login_required
def cart(request):
    cart = Cart.objects.get(user=request.user)
    cart_items = CartItems.objects.filter(cart=cart)
    total_price = sum(cart_item.pizza.price * cart_item.quantity for cart_item in cart_items)
    context = {
        'cart_items': cart_items,
        'total_price': total_price
    }
    return render(request, 'cart.html', context)



