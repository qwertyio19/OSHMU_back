from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.students.views import StudentProfileView, DiaryEntryViewSet, SendingReportViewSet, StudentCharacteristicView, StudentTitlesViewSet

router = DefaultRouter()

router.register(r'diary', DiaryEntryViewSet, basename='diary')
router.register(r'reports', SendingReportViewSet, basename='reports')
router.register(r'titles', StudentTitlesViewSet, basename='titles')

urlpatterns = [
    path('profile/', StudentProfileView.as_view(), name='student-profile'),
    path('characteristic/', StudentCharacteristicView.as_view(), name='student-characteristic'),
    path('', include(router.urls)),
]