from django.urls import path
from .views import (AllTodoView, DetailTodoView,
                    CreateTodoView, UpdateTodoView, DeleteTodoView,
                    TodaysTodo, Last10daysTodo, TodaysDoneTodo)

urlpatterns = [
    path('all_todo/', AllTodoView.as_view()),
    path('detail/<int:todo_id>', DetailTodoView.as_view()),
    path('create/', CreateTodoView.as_view()),
    path('update/<int:todo_id>/', UpdateTodoView.as_view()),
    path('delete/<int:todo_id>/', DeleteTodoView.as_view()),

    path('today-todo/', TodaysTodo.as_view()),
    path('last10-todo/', Last10daysTodo.as_view()),
    path('done-todo/', TodaysDoneTodo.as_view()),

]
