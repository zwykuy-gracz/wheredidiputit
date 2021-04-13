from django.shortcuts import render
from django.http import HttpResponse
from .models import Item


def home(request):
    return render(request, "wheredidiputit/landing.html")
    # return render(request, "wheredidiputit/base.html")

def index(request):
    item = Item.objects.all()
    context = {
        'item': item  
    }
    return render(request, 'where/items_list.html', context)
