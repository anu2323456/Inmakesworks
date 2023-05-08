from django.urls import path
from . import views
app_name='store'
urlpatterns = [

    path('',views.catallproduct,name='allproducts'),
    path('<slug:c_slug>/',views.catallproduct,name='product_by_cat'),
    path('<slug:c_slug>/<slug:prod_slug>',views.Proddetail,name='product_by_detail')
]
