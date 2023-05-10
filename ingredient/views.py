from django.shortcuts import render
from ingredient.models import Ingredient

# Create your views here.
def index(request):
    return render(request, 'ghost/index.html', {
        'Ingredient': Ingredient.objects.all()
    })