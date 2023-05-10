from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from ghost.models import Pizza


# Create your views here.
@login_required
def index(request):
    return render(request, 'ghost/index.html', {
        'Pizzas': Pizza.objects.all()
    })
