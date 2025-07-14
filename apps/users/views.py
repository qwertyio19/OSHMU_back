from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate
from apps.users.tasks import log_user_login
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import LoginSerializer, StudentCreateSerializer, FKJCreateSerializer, AdminCreateSerializer, UserSerializer
from apps.users.permissions import IsAdmin
from rest_framework.generics import CreateAPIView



class StudentCreateView(CreateAPIView):
    serializer_class = StudentCreateSerializer
    # permission_classes = [IsAdmin]

class FKJCreateView(CreateAPIView):
    serializer_class = FKJCreateSerializer
    # permission_classes = [IsAdmin]

class AdminCreateView(CreateAPIView):
    serializer_class = AdminCreateSerializer
    # permission_classes = [IsAdmin]



class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            user = authenticate(username=username, password=password)
            
            if user:
                # 👉 Отправляем задачу в Celery
                ip = request.META.get('REMOTE_ADDR')
                log_user_login.delay(user.id, ip)

                refresh = RefreshToken.for_user(user)
                return Response({
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                    'user': UserSerializer(user).data
                })

            return Response({'error': 'Неверный логин или пароль'}, status=status.HTTP_401_UNAUTHORIZED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)