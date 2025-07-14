from django.shortcuts import render
from rest_framework import viewsets
from apps.FKJ.models import Practice
from apps.FKJ.serializers import PracticeSerializer
from apps.users.permissions import FKJOnlyWritePermission



class PracticeViewSet(viewsets.ModelViewSet):
    queryset = Practice.objects.all()
    serializer_class = PracticeSerializer
    permission_classes = [FKJOnlyWritePermission]
