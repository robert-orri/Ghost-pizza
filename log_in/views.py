from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'log_in/index.html'),