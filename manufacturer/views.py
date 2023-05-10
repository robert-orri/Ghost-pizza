from django.shortcuts import render
from manufacturer.models import Offer


# Create your views here.
def index(request):
    return render(request, 'manufacturer/index.html', {
        'Offers': Offer.objects.all()
    })
