from django.urls import path
from . import views

urlpatterns = [
    # make sure to add slash at the end of address
    path('', views.index, name='index'),
    path('add-product/<int:id>/', views.add_product),
    path('shopping-cart/', views.shopping_cart),
]
