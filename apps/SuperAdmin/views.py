from rest_framework import viewsets
from .models import Institution, Faculty, Speciality, Document
from .serializers import FacultySerializer, SpecialitySerializer, InstitutionSerializer, DocumentSerializer
from rest_framework.parsers import MultiPartParser, FormParser
from apps.users.permissions import IsAdminOrFkjExceptCreate, IsAdminOrReadOnly

class InstitutionViewSet(viewsets.ModelViewSet):
    queryset = Institution.objects.all()
    serializer_class = InstitutionSerializer
    permission_classes = [IsAdminOrFkjExceptCreate]


class FacultyViewSet(viewsets.ModelViewSet):
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializer
    permission_classes = [IsAdminOrReadOnly]


class SpecialityViewSet(viewsets.ModelViewSet):
    queryset = Speciality.objects.all()
    serializer_class = SpecialitySerializer
    permission_classes = [IsAdminOrReadOnly]


class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    permission_classes = [IsAdminOrReadOnly]
