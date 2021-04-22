from django.urls import path
from .views import ItemListView, new_item, edit_item, delete_item

app_name = "where"

urlpatterns = [
    path('', ItemListView.as_view(), name='index'),
    path('new/', new_item, name='new-item'),
    path('<int:pk>/edit/', edit_item, name='edit-item'),
    path('<int:pk>/delete/', delete_item, name='delete-item'),
]