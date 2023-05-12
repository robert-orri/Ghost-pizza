from django.urls import path
from .import views
urlpatterns = [
    # http: //Localhost:8000/ghost
    path('', views.index, name='ghost-index'),
    path('<int:id>', views.get_pizza_by_id, name="pizza-details"),
    path('', views.pizza_list, name='pizza_list'),
    path('<int:pizza_id>/', views.pizza_detail, name='pizza_detail'),
    path('category/<str:category>/', views.pizza_list_by_category, name='pizza_list_by_category'),
]
