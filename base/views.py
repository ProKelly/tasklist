from django.shortcuts import render,redirect
from .models import Todo
from .forms import TodoCreationForm, LoginForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

def todo_list(request):
    query = request.GET.get('q', '')
    todos = Todo.objects.all()
    if query:
        todos = Todo.objects.filter(title__icontains=query)
    context = {'todos':todos}
    return render(request, 'base/todo_list.html', context)

@login_required(login_url='login')
def todo_create(request):
    form = TodoCreationForm()
    if request.method == 'POST':
        form = TodoCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('todo-list')
    
    context = {'form':form}
    return render(request, 'base/todo_form.html', context)

@login_required(login_url='login')
def todo_details(request, pk):
    todo = Todo.objects.get(pk=pk)
    context = {'todo':todo}
    return render(request, 'base/todo_details.html', context)

@login_required(login_url='login')
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

@login_required(login_url='login')
def todo_delete(request, pk):
    todo = Todo.objects.get(pk=pk)
    todo.delete()
    return redirect('todo-list')

def login_view(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('todo-list')
    
    context = {'form': form}
    return render(request, 'base/login.html', context)

def signup_view(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        
    context = {'form': form}
    return render(request, 'base/signup.html', context)

def logout_view(request):
    logout(request)
    return redirect('login')