from . import views
from django.urls import path



app_name = 'products'
urlpatterns = [
    path('products/', views.AllProducts.as_view(),name='products'),
]
