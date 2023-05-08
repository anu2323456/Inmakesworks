from django.urls import path
from . import views
app_name='cart'

urlpatterns=[
    path('add/<int:product_id>/',views.add_cart,name='addcart'),
    path('',views.cart_detail,name='cartdetail'),
    path('remove/<int:product_id>/',views.cart_remove,name='cartremove'),
    path('fullremove/<int:product_id>/',views.full_remove,name='fullremove'),
]
