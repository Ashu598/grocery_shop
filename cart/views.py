from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from store.models import Product
from .cart import Cart
from django.contrib import messages

@require_POST
def add_to_cart(request, product_id):
    qty = int(request.POST.get("qty", 1))
    Cart(request).add(product_id, quantity=qty)
    messages.success(request, "Added to cart.")
    return redirect("store:product_detail", slug=get_object_or_404(Product, id=product_id).slug)

def view_cart(request):
    cart = Cart(request)
    return render(request, "cart/cart.html", {"cart": cart})

@require_POST
def remove_from_cart(request, product_id):
    Cart(request).remove(product_id)
    messages.info(request, "Removed from cart.")
    return redirect("cart:view")

@require_POST
def update_qty(request, product_id):
    qty = int(request.POST.get("qty", 1))
    Cart(request).add(product_id, quantity=qty, override_qty=True)
    messages.success(request, "Quantity updated.")
    return redirect("cart:view")

def clear_cart(request):
    Cart(request).clear()
    messages.info(request, "Cart cleared.")
    return redirect("cart:view")
