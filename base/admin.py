from django.contrib import admin
from .models import Todo

@admin.register(Todo)
class Todo(admin.ModelAdmin):
    model = Todo
    fields = ['title', 'description', 'image']

# Register your models here.
