from django.shortcuts import render

pizzas = [

]

# Create your views here.
def index(request):
    return render(request, 'ghost/index.html', context={
        'pizzas': pizzas
    })