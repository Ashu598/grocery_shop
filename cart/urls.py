from django.urls import path
from . import views

urlpatterns = [
    path("", views.view_cart, name="view"),
    path("add/<int:product_id>/", views.add_to_cart, name="add"),
    path("remove/<int:product_id>/", views.remove_from_cart, name="remove"),
    path("update/<int:product_id>/", views.update_qty, name="update"),
    path("clear/", views.clear_cart, name="clear"),
]
