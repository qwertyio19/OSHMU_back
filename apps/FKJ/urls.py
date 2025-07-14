from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.FKJ.views import PracticeViewSet


router = DefaultRouter()


router.register(r'practices', PracticeViewSet, basename='practice')


urlpatterns = [
    path('', include(router.urls)),
]