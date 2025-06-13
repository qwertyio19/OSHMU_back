from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.students.views import StudentProfileView, DiaryViewSet, CharacteristicView, PracticeInfoView, DocumentViewSet

router = DefaultRouter()
router.register(r'diary', DiaryViewSet, basename='diary')
router.register(r'document', DocumentViewSet, basename='document')

urlpatterns = [
    path('profile/', StudentProfileView.as_view(), name='student-profile'),
    path('characteristic/', CharacteristicView.as_view(), name='student-characteristic'),
    path('practice/', PracticeInfoView.as_view(), name='student-practice'),
    path('', include(router.urls)),
]