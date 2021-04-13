from django.urls import path
from . import views

app_name = "where"

urlpatterns = [
    path('', views.index, name='index'),
    path('new-item', views.new_item, name='new-item'),
]