from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from .models import Item
from .forms import ItemModelForm


class ItemListView(ListView):
    template_name = 'where/items_list.html'
    queryset = Item.objects.all()
    context_object_name = "item"

@login_required
def index(request):
    item = Item.objects.all()
    context = {
        'item': item  
    }
    return render(request, 'where/items_list.html', context)


def new_item(request):
    form = ItemModelForm()
    if request.method == 'POST':
        print('creating new item')
        form = ItemModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/list')
    context = {
        'form': form,
    }
    return render(request, "where/new_item.html", context)

def edit_item(request, pk):
    item = Item.objects.get(id=pk)
    form = ItemModelForm(instance=item)
    if request.method == "POST":
        form = ItemModelForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('/list')
    context = {
        "form": form,
        "item": item,
    }
    return render(request, "where/edit_item.html", context)

def delete_item(request, pk):
    item = Item.objects.get(id=pk)
    item.delete()
    return redirect('/list')