from django.urls import path
from .import views
urlpatterns = [
    # http: //Localhost:8000/ghost
    path('', views.index, name='ghost-index'),
    path('<int:id>', views.get_pizza_by_id, name="pizza-details"),
]
