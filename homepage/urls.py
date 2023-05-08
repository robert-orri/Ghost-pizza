from django.urls import path
from .import views
urlpatterns = [
    # http: //Localhost:8000/homepage
    path('', views.index, name='homepage-index'),
]
