from django.urls import path
from . import views

app_name = 'todo'

urlpatterns = [
    path('', views.get_todo_list, name='home'),
    path('add', views.add_item, name='add'),
    path('edit/<itemId>', views.edit_item, name='edit'),
    path('toggle/<itemId>', views.toggle_item, name='toggle'),
    path('delete/<itemId>', views.delete_item, name='delete')
]
