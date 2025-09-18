from .cart import Cart

def cart_summary(request):
    cart = Cart(request)
    return {"cart_summary": {"count": len(cart), "total": cart.get_total_price()}}
