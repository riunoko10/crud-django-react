from rest_framework import viewsets
from .serializer import TaskSerializer
from .models import Task
from rest_framework import viewsets, pagination
from .serializer import TaskSerializer
from .models import Task

# Create your views here.

# Create your views here.

class TaskListView(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    pagination_class = pagination.PageNumberPagination