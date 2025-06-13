# views.py
from rest_framework import viewsets
from .models import Institution, Course, Day, Task
from .serializers import InstitutionSerializer, CourseSerializer, DaySerializer, TaskSerializer
from rest_framework.parsers import MultiPartParser, FormParser


class InstitutionViewSet(viewsets.ModelViewSet):
    queryset = Institution.objects.all()
    serializer_class = InstitutionSerializer
    parser_classes = [MultiPartParser, FormParser]  # важно для загрузки файлов

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class DayViewSet(viewsets.ModelViewSet):
    queryset = Day.objects.all()
    serializer_class = DaySerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer