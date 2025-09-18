from decimal import Decimal
from store.models import Product

CART_SESSION_ID = "cart"

class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(CART_SESSION_ID)
        if not cart:
            cart = self.session[CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, product_id, quantity=1, override_qty=False):
        product = Product.objects.get(id=product_id)
        pid = str(product_id)
        if pid not in self.cart:
            self.cart[pid] = {"name": product.name, "price": str(product.price), "qty": 0}
        if override_qty:
            self.cart[pid]["qty"] = quantity
        else:
            self.cart[pid]["qty"] += quantity
        self.save()

    def remove(self, product_id):
        pid = str(product_id)
        if pid in self.cart:
            del self.cart[pid]
            self.save()

    def clear(self):
        self.session[CART_SESSION_ID] = {}
        self.session.modified = True

    def save(self):
        self.session[CART_SESSION_ID] = self.cart
        self.session.modified = True

    def __iter__(self):
        pids = self.cart.keys()
        products = Product.objects.filter(id__in=pids)
        for product in products:
            item = self.cart[str(product.id)]
            item["product"] = product
            item["price"] = Decimal(item["price"])
            item["total"] = item["price"] * item["qty"]
            yield item

    def __len__(self):
        return sum(item["qty"] for item in self.cart.values())

    def get_total_price(self):
        from decimal import Decimal
        return sum(Decimal(item["price"]) * item["qty"] for item in self.cart.values())
