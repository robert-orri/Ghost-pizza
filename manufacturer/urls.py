from django.urls import path
from .import views
urlpatterns = [
    # http: //Localhost:8000/manufacturer
    path('', views.index, name='manufacturer-index'),
]

