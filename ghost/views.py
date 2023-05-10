from django.shortcuts import render
from ghost.models import Pizza


# Create your views here.
def index(request):
    return render(request, 'ghost/index.html', {
        'Pizzas': Pizza.objects.all()
    })
