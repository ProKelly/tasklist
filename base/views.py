from django.shortcuts import render,redirect
from .models import Todo
from .forms import TodoCreationForm

def todo_list(request):
    todos = Todo.objects.all()
    context = {'todos':todos}
    return render(request, 'base/todo_list.html', context)

def todo_create(request):
    form = TodoCreationForm()
    if request.method == 'POST':
        form = TodoCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('todo-list')
    
    context = {'form':form}
    return render(request, 'base/todo_form.html', context)

def todo_details(request, pk):
    todo = Todo.objects.get(pk=pk)
    context = {'todo':todo}
    return render(request, 'base/todo_details.html', context)

def todo_update(request, pk):
    todo = Todo.objects.get(pk=pk)
    form = TodoCreationForm(instance=todo)
    if request.method == 'POST':
        form = TodoCreationForm(request.POST, request.FILES, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('todo-details', pk=pk)
    
    context = {'form':form, 'todo':todo}
    return render(request, 'base/todo_form.html', context)

def todo_delete(request, pk):
    todo = Todo.objects.get(pk=pk)
    todo.delete()
    return redirect('todo-list')
