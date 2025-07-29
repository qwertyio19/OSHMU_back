from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.students.views import SendingReportViewSet, StudentTitlesViewSet, StudentProfileView, MyPracticeListAPIView, CharacteristicsViewSet


router = DefaultRouter()


router.register(r'reports', SendingReportViewSet, basename='reports')
router.register(r'titles', StudentTitlesViewSet, basename='titles')
router.register(r'characteristics', CharacteristicsViewSet, basename='characteristics')



urlpatterns = [
    path('profile/', StudentProfileView.as_view(), name='student-profile'),
    path('my_practices/', MyPracticeListAPIView.as_view(), name='my-practices'),
    path('', include(router.urls)),
]