from django.urls import path
from .import views
urlpatterns = [
    # http: //Localhost:8000/log_in
    path('', views.index, name='log_in-index')
]