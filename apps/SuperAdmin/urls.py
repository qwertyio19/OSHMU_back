# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import InstitutionViewSet, CourseViewSet, DayViewSet, TaskViewSet

router = DefaultRouter()
router.register(r'institutions', InstitutionViewSet)
router.register(r'courses', CourseViewSet)
router.register(r'days', DayViewSet)
router.register(r'tasks', TaskViewSet)

urlpatterns = [
    path('', include(router.urls)),
]