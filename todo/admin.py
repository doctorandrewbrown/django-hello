from django.contrib import admin
from .models import Item
# Register your models here.
# Registering Item model to make available to admin panel
admin.site.register(Item)