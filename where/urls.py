from django.urls import path
from .views import (
    ItemListView, EditItemView, NewItemView, ItemDeleteView,
    new_item, edit_item, delete_item
)

app_name = "where"

urlpatterns = [
    path('', ItemListView.as_view(), name='index'),
    path('new/', NewItemView.as_view(), name='new-item'),
    path('<int:pk>/edit/', EditItemView.as_view(), name='edit-item'),
    path('<int:pk>/delete/', delete_item, name='delete-item'),
]