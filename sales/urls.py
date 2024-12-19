from django.urls import path, include
from . import views

urlpatterns = [
    path('products/', views.ProductListCreate.as_view(), name="product-view-create"),
    path('sales/', views.SaleListCreate.as_view(), name="sale-view-create"),

]
