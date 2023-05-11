from django.shortcuts import render, get_object_or_404
from ghost.models import Pizza, PizzaIngredient,Ingredient
from django.http import JsonResponse


# Create your views here.
def index(request):
    if 'search_filter' in request.GET:
        search_filter = request.GET['search_filter']
        pizzas = list(Pizza.objects.filter(name__icontains=search_filter).values())
        return JsonResponse({'data': pizzas})
    return render(request, 'ghost/index.html', {
        'Pizzas': Pizza.objects.all()
    })

def get_pizza_by_id(request, id):
    pizza = Pizza.objects.get(pk=id).pizzaingredient_set.all()
    ingredients = []
    for p in pizza:
        ingredients.append(Ingredient.objects.get(pk=p.ingredient_id))
    #ingredient = PizzaIngredient.objects.get(pizza_id=id)
    #print(ingredient)
    return render(request, 'ghost/pizza_details.html', {
        'Pizza': get_object_or_404(Pizza, pk=id),
        'Ingredients':ingredients
    })
