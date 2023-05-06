from django.shortcuts import render

offers = [
    {'name': '2 for 1', 'price': '4500'},
    {'name': 'Ghost Challenge', 'price': '3500'},
    {'name': 'Family offer', 'price': '6000'}

]

# Create your views here.
def index(request):
    return render(request, 'manufacturer/index.html', context={
        'offers': offers
    })