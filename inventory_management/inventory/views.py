from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.

from .models import *

#from .forms import *



def index(request):
    return render(request, 'calendar.html')

def display_resturant(request):
    items = Resturant.objects.all()
    context = {
        'items': items,
        'header': 'Resturant',
    }
    return render(request, 'calendar.html', context)