from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Item
from .forms import ItemModelForm


class ItemListView(LoginRequiredMixin, ListView):
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


class NewItemView(LoginRequiredMixin, CreateView):
    template_name = 'where/new_item.html'
    form_class = ItemModelForm

    def get_success_url(self):
        return reverse('where:index')

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


class EditItemView(LoginRequiredMixin, UpdateView):
    template_name = 'where/edit_item.html'
    queryset = Item.objects.all()
    form_class = ItemModelForm

    def get_success_url(self):
        return reverse('where:index')

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


# delete template się nie ładuje - od razu usuwa
class ItemDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'where/delete_item.html'
    print('+1+')
    queryset = Item.objects.all()
    print('+2+')

    def get_success_url(self):
        return reverse('where:index')

def delete_item(request, pk):
    item = Item.objects.get(id=pk)
    item.delete()
    return redirect('/list')