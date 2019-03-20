from django.urls import path, include
from .views import add_to_cart, OrderView, cart_delete, update_quantity, OrderCreateView, SuccessView

urlpatterns = [
    path('add_to_cart/<product_id>/', add_to_cart, name='add_to_cart'),
    path('order/', OrderView.as_view(), name='order'),
    path('delete_item/<item_id>/', cart_delete, name='cart_delete'),
    path('update_q/<item_id>/', update_quantity, name='update_quantity'),
    path('create_order/', OrderCreateView.as_view(), name='create_order'),
    path('order_success/', SuccessView.as_view(), name='success'),
]
