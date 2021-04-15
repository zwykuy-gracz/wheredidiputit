from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Item


# def home(request):
#     return render(request, "landing.html")

def home(request):
    return render(request, "home.html")

@login_required
def index(request):
    item = Item.objects.all()
    context = {
        'item': item  
    }
    return render(request, 'where/items_list.html', context)

def new_item(request):
    return render(request, "where/new_item.html")