from django.shortcuts import render


# Create your views here.
def get_todo_list(request):
    context = {}
    return render(request, 'todo/home.html', context)