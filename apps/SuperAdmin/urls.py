
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import InstitutionViewSet, FacultyViewSet, SpecialityViewSet, DocumentViewSet

router = DefaultRouter()
router.register(r'institutions', InstitutionViewSet, basename='add_institutions')
router.register(r'faculty', FacultyViewSet, basename='faculty')
router.register(r'speciality', SpecialityViewSet, basename='speciality')
router.register(r'documents', DocumentViewSet, basename='document')

urlpatterns = [
    path('', include(router.urls)),
]