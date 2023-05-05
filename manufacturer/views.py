from django.shortcuts import render
# Create your views here.

offers = [
    {'name': '2 for 1', 'price': '4500'},
    {'name': 'Ghost Challenge', 'price': '3500'},
    {'name': 'Family offer', 'price': '6000'}
]
def index(request):
    return render(request, 'ghost/index.html', context={
        'offers': offers
    })
