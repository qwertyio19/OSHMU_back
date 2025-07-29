from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.FKJ.views import PracticeViewSet, TitlesFkjViewSet, StudentListView


router = DefaultRouter()


router.register(r'practices', PracticeViewSet, basename='practice')
router.register(r'titles', TitlesFkjViewSet, basename='titles-fkj')


urlpatterns = [
    path('students/', StudentListView.as_view(), name='student-list'),
    path('', include(router.urls)),
]