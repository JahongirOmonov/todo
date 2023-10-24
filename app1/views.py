from rest_framework import views
from .serializers import TodoSerializer
from .models import TodoModel
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status
import datetime


class AllTodoView(views.APIView):
    def get(self, request):
        all_todos = TodoModel.objects.all()
        serializer = TodoSerializer(all_todos, many=True)
        return Response(serializer.data)


class DetailTodoView(views.APIView):
    def get(self, request, *args, **kwargs):
        todo = get_object_or_404(TodoModel, id=kwargs['todo_id'])
        serializer = TodoSerializer(todo)
        return Response(serializer.data)


class CreateTodoView(views.APIView):
    def post(self, request):
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class UpdateTodoView(views.APIView):
    def patch(self, request, *args, **kwargs):
        todo = get_object_or_404(TodoModel, id=kwargs['todo_id'])
        serializer = TodoSerializer(todo, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class DeleteTodoView(views.APIView):
    def delete(self, request, *args, **kwargs):
        todo = get_object_or_404(TodoModel, id=kwargs['todo_id'])

        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class TodaysTodo(views.APIView):
    def get(self, request, *args, **kwargs):
        today = datetime.date.today()
        todos = TodoModel.objects.filter(created_at__date=today)

        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data)


class Last10daysTodo(views.APIView):
    def get(self, request, *args, **kwargs):
        today = datetime.datetime.now()
        last_ten = today - datetime.timedelta(days=10)
        todos = TodoModel.objects.filter(created_at__gte=last_ten, created_at__lte=today)
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data)


class TodaysDoneTodo(views.APIView):
    def get(self, request, *args, **kwargs):
        today = datetime.date.today()
        todos = TodoModel.objects.filter(created_at__date=today, status=True)
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data)
