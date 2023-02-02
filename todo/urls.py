from django.urls import path
from . import views

app_name = 'todo'

urlpatterns = [
    path('', views.get_todo_list, name='home'),
]
