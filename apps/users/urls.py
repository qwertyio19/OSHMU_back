from django.urls import path, include
from apps.users.views import LoginView, StudentCreateView, FKJCreateView, AdminCreateView
from rest_framework.routers import DefaultRouter


router = DefaultRouter()


urlpatterns = [
    path('', include(router.urls)),
    path('login/', LoginView.as_view(), name='api-login'),
    path('create/student/', StudentCreateView.as_view()),
    path('create/fkj/', FKJCreateView.as_view()),
    path('create/admin/', AdminCreateView.as_view()),
]
