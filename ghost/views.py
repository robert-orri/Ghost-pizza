from django.shortcuts import render

pizzas = [
    {'name': 'Margarita', 'price': '2500'},
    {'name': 'Pepperoni', 'price': '2700'},
    {'name': 'Hawaiian', 'price': '2600'}

]

# Create your views here.
def index(request):
    return render(request, 'ghost/index.html', context={
        'pizzas': pizzas
    })