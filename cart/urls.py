from django.urls import path
from .import views
urlpatterns = [
    # http: //Localhost:8000/cart
    path('', views.index, name='cart-index')
]