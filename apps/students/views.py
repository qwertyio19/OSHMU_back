from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from apps.users.permissions import IsAdmin, IsStudentOrReadOnly, IsAdminOrReadOnly
from apps.students.models import StudentProfile, DiaryEntry, StudentCharacteristic, SendingReport, StudentTitles
from apps.students.serializers import StudentProfileSerializer, DiaryEntrySerializer, StudentCharacteristicSerializer, SendingReportSerializer, StudentTitlesSerializer
from apps.users.tasks import process_sending_report


class StudentProfileView(APIView):
    permission_classes = [permissions.AllowAny]

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
    permission_classes = [IsStudentOrReadOnly]

    def get_queryset(self):
        return DiaryEntry.objects.all()

    def perform_create(self, serializer):
        student = StudentProfile.objects.first()
        serializer.save(student=student)


class StudentTitlesViewSet(viewsets.ModelViewSet):
    serializer_class = StudentTitlesSerializer
    permission_classes = [IsAdminOrReadOnly]
    queryset = StudentTitles.objects.all()


class SendingReportViewSet(viewsets.ModelViewSet):
    serializer_class = SendingReportSerializer
    permission_classes = [IsStudentOrReadOnly]
    queryset = SendingReport.objects.all()

    def perform_create(self, serializer):
        report = serializer.save()
        process_sending_report.delay(report.id)


class StudentCharacteristicView(APIView):
    permission_classes = [IsStudentOrReadOnly]

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
    


