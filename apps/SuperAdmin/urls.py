
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import InstitutionViewSet, FacultyViewSet, SpecialityViewSet, DocumentViewSet, TitlesAdminViewSet, LanguageViewSet

router = DefaultRouter()
router.register(r'institutions', InstitutionViewSet, basename='add_institutions')
router.register(r'faculty', FacultyViewSet, basename='faculty')
router.register(r'speciality', SpecialityViewSet, basename='speciality')
router.register(r'documents', DocumentViewSet, basename='document')
router.register(r'titles', TitlesAdminViewSet, basename='titles_admin')
router.register(r'languages', LanguageViewSet, basename='language')


urlpatterns = [
    path('', include(router.urls)),
]