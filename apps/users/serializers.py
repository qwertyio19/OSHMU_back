from rest_framework import serializers
from .models import User
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import serializers



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('role')