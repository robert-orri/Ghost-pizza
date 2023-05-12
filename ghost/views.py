from django.shortcuts import render, get_object_or_404
from ghost.models import Pizza, PizzaIngredient,Ingredient
from django.http import JsonResponse


# Create your views here.
def index(request):
    if 'search_filter' in request.GET:
        search_filter = request.GET['search_filter']
        print("asdf")
        pizzas = [{
            'id': x.id,
            'name': x.name,
            'description': x.description,
            'image': x.image,
            'price': x.price,
            'second_image': x.second_image
        } for x in Pizza.objects.filter(name__icontains=search_filter)]
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

def pizza_list(request):
    pizzas = Pizza.objects.all()
    return render(request, 'ghost/index.html', {'pizzas': pizzas})

def pizza_detail(request, pizza_id):
    pizza = get_object_or_404(Pizza, id=pizza_id)
    return render(request, 'ghost/index.html', {'pizza': pizza})

def pizza_list_by_category(request, category):
    pizzas = Pizza.objects.filter(category=category)
    return render(request, 'ghost/index.html', {'Pizzas': pizzas})