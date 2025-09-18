from django.contrib import admin
from django.urls import path, include
from store.views import product_list
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include(("accounts.urls", "accounts"), namespace="accounts")),
    path("cart/", include(("cart.urls", "cart"), namespace="cart")),
    path("orders/", include(("orders.urls", "orders"), namespace="orders")),
    path("", include(("store.urls", "store"), namespace="store")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
