
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import InstitutionViewSet, CourseViewSet, DayViewSet, TaskViewSet

router = DefaultRouter()
router.register(r'institutions', InstitutionViewSet, basename='add_institutions')
router.register(r'courses', CourseViewSet, basename='courses')
router.register(r'days', DayViewSet, basename='days')
router.register(r'tasks', TaskViewSet, basename='tasks')

urlpatterns = [
    path('', include(router.urls)),
]