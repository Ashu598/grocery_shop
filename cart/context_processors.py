from .models import Cart

def cart(request):
    cart_id = request.session.get("cart_id")
    cart = None
    if cart_id:
        try:
            cart = Cart.objects.get(id=cart_id)
        except Cart.DoesNotExist:
            cart = None
    return {"cart": cart}
