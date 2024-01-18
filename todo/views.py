from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from todo.models import Item
from .forms import ItemForm


# Say hello view.
def say_hello(request):
    return HttpResponse("hello django")


# Todo list view.
def todo_list(request):
    # Get all data from Item table
    items = Item.objects.all()
    # Put items into django context (list) object
    context = {"items": items}
    return render(request, "./todo/todo_list.html", context)


# Edit item view.
def edit_item(request, item_id):
    if request.method == "POST":
        # get existing data from db for given id
        data = get_object_or_404(Item, pk=item_id)
        # Create instance of form and get user edit data
        form = ItemForm(request.POST, instance=data)
        # Then compare data input with model
        if form.is_valid():
            # Save new item to database with no need for ORM
            form.save()
        return redirect("todo_list")
    # Create instance of form
    form = ItemForm()
    # get existing data from db for given id
    data = get_object_or_404(Item, pk=item_id)
    print(data)
    # populate form with existing data from db
    form = ItemForm(instance=data)
    # Put form variable in context to pass on rendering
    context = {"form": form, "item_id": item_id}
    return render(request, "./todo/edit_item.html", context)


# Add item view.
def add_item(request):
    if request.method == "POST":
        # Create instance of form and populate with input data from form fields
        form = ItemForm(request.POST)
        # Then compare data input with model
        if form.is_valid():
            # Save new item to database with no need for ORM
            form.save()
        return redirect("todo_list")
    # Create instance of form for user input
    form = ItemForm()
    # Put form variable in context to pass on rendering
    context = {"form": form}
    return render(request, "./todo/add_item.html", context)
