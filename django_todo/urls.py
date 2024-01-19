"""django_todo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
# Import view functions
from todo.views import todo_list, add_item, say_hello, edit_item, toggle_item, delete_item
urlpatterns = [
    path('admin/', admin.site.urls),
    # empty "" url triggers say_hello view
    path("", say_hello, name="say_hello"),
    path("list", todo_list, name="todo_list"),
    path("add", add_item, name="add_item"),
    path("edit/<item_id>", edit_item, name="edit_item"),
    path("toggle/<item_id>", toggle_item, name="toggle_item"),
    path("delete/<item_id>", delete_item, name="delete_item")
]
