from rest_framework import viewsets
from .models import Institution, Course, Day, Task
from .serializers import InstitutionSerializer, CourseSerializer, DaySerializer, TaskSerializer
from rest_framework.parsers import MultiPartParser, FormParser
from apps.users.permissions import IsAdmin, IsFkj, IsFkjOrReadOnly

class InstitutionViewSet(viewsets.ModelViewSet):
    queryset = Institution.objects.all()
    serializer_class = InstitutionSerializer
    parser_classes = [MultiPartParser, FormParser]
    permission_classes = [IsAdmin]  # Только админы могут управлять учреждениями

    def perform_create(self, serializer):
        # Автоматически связываем учреждение с текущим пользователем (админом)
        serializer.save(user=self.request.user)

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsFkj] 

class DayViewSet(viewsets.ModelViewSet):
    queryset = Day.objects.all()
    serializer_class = DaySerializer
    permission_classes = [IsFkj] 

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsFkjOrReadOnly]  