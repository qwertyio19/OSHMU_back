from django.shortcuts import render
from rest_framework import viewsets
from apps.FKJ.models import Practice, TitlesFkj
from apps.FKJ.serializers import PracticeSerializer, TitlesFkjSerializer
from apps.users.permissions import FKJOnlyWritePermission, IsAdmin



class PracticeViewSet(viewsets.ModelViewSet):
    queryset = Practice.objects.all()
    serializer_class = PracticeSerializer
    permission_classes = [FKJOnlyWritePermission]


class TitlesFkjViewSet(viewsets.ModelViewSet):
    queryset = TitlesFkj.objects.all()
    serializer_class = TitlesFkjSerializer
    permission_classes = [IsAdmin]
