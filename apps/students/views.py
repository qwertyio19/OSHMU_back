from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from apps.students.models import StudentProfile, DiaryEntry, StudentCharacteristic, PracticeInfo, Document
from apps.students.serializers import  PracticeInfoSerializer, StudentProfileSerializer, DiaryEntrySerializer, StudentCharacteristicSerializer, DocumentSerializer
from django.core.cache import cache
from django.http import HttpResponse

class StudentProfileView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        profile = StudentProfile.objects.get(user=request.user)
        serializer = StudentProfileSerializer(profile)
        return Response(serializer.data)

    def put(self, request):
        profile = StudentProfile.objects.get(user=request.user)
        serializer = StudentProfileSerializer(profile, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

class DocumentViewSet(viewsets.ModelViewSet):
    serializer_class = DocumentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Document.objects.filter(student__user=self.request.user)

    def perform_create(self, serializer):
        profile = StudentProfile.objects.get(user=self.request.user)
        serializer.save(student=profile)


class DiaryViewSet(viewsets.ModelViewSet):
    serializer_class = DiaryEntrySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return DiaryEntry.objects.filter(student__user=self.request.user)

    def perform_create(self, serializer):
        profile = StudentProfile.objects.get(user=self.request.user)
        serializer.save(student=profile)


class CharacteristicView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        obj = StudentCharacteristic.objects.get(student__user=request.user)
        serializer = StudentCharacteristicSerializer(obj)
        return Response(serializer.data)

    def put(self, request):
        obj = StudentCharacteristic.objects.get(student__user=request.user)
        serializer = StudentCharacteristicSerializer(obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)


class PracticeInfoView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        obj = PracticeInfo.objects.get(student__user=request.user)
        serializer = PracticeInfoSerializer(obj)
        return Response(serializer.data)

    def put(self, request):
        obj = PracticeInfo.objects.get(student__user=request.user)
        serializer = PracticeInfoSerializer(obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

def test_cache(request):
    cache.set('my_key', 'hello redis', 30) 
    value = cache.get('my_key')
    return HttpResponse(f'Cached value: {value}')
