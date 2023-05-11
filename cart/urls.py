from django.urls import path
from .import views
urlpatterns = [
    # http: //Localhost:8000/cart
    path('', views.index, name='cart-index'),
    path('add-to-cart/<int:pizza_id>/', views.add_to_cart, name='add_to_cart'),
]