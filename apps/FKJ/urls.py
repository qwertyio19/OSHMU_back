from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.FKJ.views import PracticeViewSet, TitlesFkjViewSet


router = DefaultRouter()


router.register(r'practices', PracticeViewSet, basename='practice')
router.register(r'titles', TitlesFkjViewSet, basename='titles-fkj')


urlpatterns = [
    path('', include(router.urls)),
]