from django.shortcuts import render, redirect, get_object_or_404
from .models import Item
from .forms import ItemForm

# Create your views here.


def get_todo_list(request):
    items = Item.objects.all()
    context = {'items': items}
    return render(request, 'todo/home.html', context)


def add_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo:home')
    form = ItemForm()
    context = {'form': form}
    return render(request, 'todo/add_item.html', context)


def edit_item(request, itemId):
    item = get_object_or_404(Item, id=itemId)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('todo:home')
    form = ItemForm(instance=item)
    return render(request, 'todo/edit_item.html', context={'form': form})


def toggle_item(request, itemId):
    item = get_object_or_404(Item, id=itemId)
    item.done = not item.done
    item.save()
    return redirect('todo:home')


def delete_item(request, itemId):
    item = get_object_or_404(Item, id=itemId)
    item.delete()
    return redirect('todo:home')