from rest_framework import viewsets, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from apps.FKJ.models import Practice
from apps.FKJ.serializers import PracticeSerializer
from apps.users.permissions import IsStudentOrReadOnly, IsAdminOrReadOnly
from apps.students.models import SendingReport, StudentTitles, Characteristics
from apps.students.serializers import SendingReportSerializer, StudentTitlesSerializer, StudentProfileSerializer, CharacteristicsSerializer
from apps.users.tasks import process_sending_report
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from rest_framework.generics import RetrieveAPIView
from rest_framework.parsers import MultiPartParser, FormParser



class MyPracticeListAPIView(generics.ListAPIView):
    permission_classes = [IsStudentOrReadOnly]
    serializer_class = PracticeSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_anonymous:
            return Practice.objects.none()
        return Practice.objects.filter(students=user)


class StudentTitlesViewSet(viewsets.ModelViewSet):
    serializer_class = StudentTitlesSerializer
    permission_classes = [IsAdminOrReadOnly]
    queryset = StudentTitles.objects.all()


class SendingReportViewSet(viewsets.ModelViewSet):
    serializer_class = SendingReportSerializer
    permission_classes = [IsStudentOrReadOnly]
    queryset = SendingReport.objects.all()
    parser_classes = [MultiPartParser, FormParser]

    def perform_create(self, serializer):
        report = serializer.save()
        # process_sending_report.delay(report.id)


class StudentProfileView(RetrieveAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        if user.role != 'student':
            raise PermissionDenied('Доступ разрешён только студентам.')
        serializer = StudentProfileSerializer(user)
        return Response(serializer.data)
    

class CharacteristicsViewSet(viewsets.ModelViewSet):
    serializer_class = CharacteristicsSerializer
    permission_classes = [IsStudentOrReadOnly]
    queryset = Characteristics.objects.all()