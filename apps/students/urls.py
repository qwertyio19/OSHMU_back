from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.students.views import StudentProfileView, DiaryEntryViewSet, SendingRaportViewSet, StudentCharacteristicView

router = DefaultRouter()

router.register(r'diary', DiaryEntryViewSet, basename='diary')
router.register(r'reports', SendingRaportViewSet, basename='reports')

urlpatterns = [
    path('profile/', StudentProfileView.as_view(), name='student-profile'),
    path('characteristic/', StudentCharacteristicView.as_view(), name='student-characteristic'),
    path('', include(router.urls)),
]