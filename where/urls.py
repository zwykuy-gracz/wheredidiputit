from django.urls import path
from . import views

app_name = "where"

urlpatterns = [
    path('', views.index, name='index'),
    path('new-item/', views.new_item, name='new-item'),
    path('<int:pk>/edit/', views.edit_item, name='edit-item'),
    path('<int:pk>/delete/', views.delete_item, name='delete-item'),
]