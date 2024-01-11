from django.shortcuts import render, HttpResponse
from todo.models import Item

# Say hello view.
def say_hello(request):
    return HttpResponse("hello django")

# Todo list view.
def todo_list(request):
    # Get all data from Item table
    items = Item.objects.all()
    # Put items into django context (list) object
    context = {"items":items}
    return render(request, "./todo/todo_list.html", context)

# Add item view.
def add_item(request):
    #print(request.name)
    return render(request, "./todo/add_item.html")