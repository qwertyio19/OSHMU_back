from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate
from apps.users.tasks import log_user_login
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import AdminDetailSerializer, FKJDetailSerializer, LoginSerializer, StudentCreateSerializer, FKJCreateSerializer, AdminCreateSerializer, StudentDetailSerializer, UserSerializer
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
            print("✅ Serializer passed")
            user = serializer.validated_data['user']
            print(f"🔐 User: {user}, role: {user.role}")

            # IP лог
            ip = request.META.get('REMOTE_ADDR', '0.0.0.0')
            print("🌍 IP:", ip)
            # log_user_login.delay(user.id, ip)

            # JWT
            refresh = RefreshToken.for_user(user)

            # Сериализация по роли
            role = user.role.lower() if user.role else ''
            if role == 'admin':
                user_data = AdminDetailSerializer(user).data
            elif role == 'fkj':
                user_data = FKJDetailSerializer(user).data
            elif role == 'student':
                user_data = StudentDetailSerializer(user).data
            else:
                user_data = {'id': user.id,
                             'full_name': user.full_name, 'role': user.role}

            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'user': user_data
            })

        print("❌ Errors:", serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

