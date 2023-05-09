from django.urls import path
from .import views
urlpatterns = [
    # http: //Localhost:8000/ghost
    path('', views.index, name='log_in-index'),
]