from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from apps.users.permissions import IsAdmin

from django.shortcuts import get_object_or_404

from apps.students.models import StudentProfile, DiaryEntry, StudentCharacteristic, SendingRaport
from apps.students.serializers import StudentProfileSerializer, DiaryEntrySerializer, StudentCharacteristicSerializer, SendingRaportSerializer


class StudentProfileView(APIView):
    permission_classes = [permissions.AllowAny]  # <-- Отключено

    def get(self, request):
        profile = StudentProfile.objects.first()
        serializer = StudentProfileSerializer(profile)
        return Response(serializer.data)

    def put(self, request):
        profile = StudentProfile.objects.first()
        serializer = StudentProfileSerializer(profile, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class DiaryEntryViewSet(viewsets.ModelViewSet):
    serializer_class = DiaryEntrySerializer
    permission_classes = [permissions.AllowAny]  # <-- Отключено

    def get_queryset(self):
        return DiaryEntry.objects.all()

    def perform_create(self, serializer):
        student = StudentProfile.objects.first()
        serializer.save(student=student)


class SendingRaportViewSet(viewsets.ModelViewSet):
    serializer_class = SendingRaportSerializer
    permission_classes = [permissions.AllowAny]  # <-- Отключено
    queryset = SendingRaport.objects.all()


class StudentCharacteristicView(APIView):
    permission_classes = [permissions.AllowAny]  # <-- Отключено

    def get(self, request):
        obj = StudentCharacteristic.objects.first()
        serializer = StudentCharacteristicSerializer(obj)
        return Response(serializer.data)

    def put(self, request):
        obj = StudentCharacteristic.objects.first()
        serializer = StudentCharacteristicSerializer(obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


