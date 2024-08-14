from django.urls import path
from . import views

urlpatterns = [
    path('', views.todo_list, name='todo-list'),
    path('create/', views.todo_create, name='create-todo'),
    path('todos/<str:pk>/details/', views.todo_details, name='todo-details'),
    path('todos/<str:pk>/update/', views.todo_update, name='todo-update'),
    path('todos/<str:pk>/delete/', views.todo_delete, name='todo-delete'),
]
