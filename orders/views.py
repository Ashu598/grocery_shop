from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from django.db import transaction
from .models import Order, OrderItem
from cart.cart import Cart

@login_required
def checkout(request):
    cart = Cart(request)
    if len(cart) == 0:
        messages.info(request, "Your cart is empty.")
        return redirect("cart:view")

    if request.method == "POST":
        full_name = request.POST.get("full_name")
        address = request.POST.get("address")
        city = request.POST.get("city")
        pincode = request.POST.get("pincode")

        with transaction.atomic():
            order = Order.objects.create(
                user=request.user,
                full_name=full_name,
                address=address,
                city=city,
                pincode=pincode,
                total_amount=cart.get_total_price(),
            )
            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item["product"],
                    price=item["price"],
                    quantity=item["qty"],
                )
            cart.clear()

        messages.success(request, "Order placed successfully!")
        return redirect("orders:success", order_id=order.id)

    return render(request, "orders/checkout.html", {"cart": cart})

@login_required
def order_success(request, order_id):
    return render(request, "orders/order_success.html", {"order_id": order_id})

@login_required
def order_history(request):
    orders = request.user.orders.all()
    return render(request, "orders/order_history.html", {"orders": orders})
