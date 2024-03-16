from . import views
from django.urls import path



app_name = 'products'
urlpatterns = [
    path('products/', views.AllProducts.as_view(),name='products'),
    path('product/<int:pk>/', views.EditProduct.as_view(),name='edit_products'),

]
