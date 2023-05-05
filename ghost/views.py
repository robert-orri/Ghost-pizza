from django.shortcuts import render

pizzas = [
    {'name': 'Margarita', 'price': '2500kr'},
    {'name': 'Pepperoni', 'price': '2700kr'},
    {'name': 'Hawaiian', 'price': '2600kr'}

]

# Create your views here.
def index(request):
    return render(request, 'ghost/index.html', context={
        'pizzas': pizzas
    })