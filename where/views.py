from django.shortcuts import render
from django.http import HttpResponse
from .models import Item

def index(request):
    item = Item.objects.all()
    context = {
        'item': item
    }
    return render(request, 'where/base.html', context)