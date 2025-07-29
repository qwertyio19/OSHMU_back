from django.shortcuts import render
from rest_framework import viewsets, generics
from apps.FKJ.models import Practice, TitlesFkj
from apps.FKJ.serializers import PracticeSerializer, TitlesFkjSerializer, ShortStudentSerializer
from apps.users.permissions import FKJOnlyWritePermission, IsAdmin
from apps.users.models import User


class PracticeViewSet(viewsets.ModelViewSet):
    queryset = Practice.objects.all()
    serializer_class = PracticeSerializer
    # permission_classes = [FKJOnlyWritePermission]


class StudentListView(generics.ListAPIView):
    queryset = User.objects.filter(role='student')
    serializer_class = ShortStudentSerializer


class TitlesFkjViewSet(viewsets.ModelViewSet):
    queryset = TitlesFkj.objects.all()
    serializer_class = TitlesFkjSerializer
    permission_classes = [IsAdmin]
