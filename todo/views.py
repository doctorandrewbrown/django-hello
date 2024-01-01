from django.shortcuts import render, HttpResponse
from todo.models import Item

# Say hello view.
def say_hello(request):
    return HttpResponse("hello django")

# Todo list view.
def todo_list(request):
    items = Item.objects.all()
    context = {"items":items}
    return render(request, "./todo/todo_list.html", context)