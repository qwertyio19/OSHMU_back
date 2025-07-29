import random
from rest_framework import serializers
from rest_framework import serializers
from apps.users.models import User


class AdminDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'full_name', 'role']


class FKJDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'full_name', 'role', 'faculty']


class StudentDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'full_name', 'student_number', 'course', 'institution', 'speciality', 'role']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'full_name', 'login_fkj', 'student_number', 'password', 'course', 'faculty', 'role', 'institution', 'speciality']
        extra_kwargs = {
            'full_name': {'label': 'Полное имя'},
            'password': {'write_only': True, 'label': 'Пароль'},
            'faculty': {'label': 'Факультет'},
            'role': {'label': 'Роль'}
        }

    def create(self, validated_data):
        if 'username' not in validated_data:
            full_name = validated_data.get('full_name', '')
            username = full_name.replace(' ', '_').lower()
            validated_data['username'] = username

        return User.objects.create_user(**validated_data)
    
    def to_representation(self, instance):
        data = super().to_representation(instance)
        if instance.role != 'fkj':
            data.pop('faculty', None)
        return data


class StudentCreateSerializer(UserSerializer):
    class Meta:
        model = User
        fields = ['id', 'full_name', 'student_number', 'password', 'course', 'role', 'institution', 'speciality']
        extra_kwargs = {
            'full_name': {'label': 'Полное имя'},
            'password': {'write_only': True, 'label': 'Пароль'},
            'role': {'label': 'Роль'}
        }

    def validate(self, attrs):
        attrs['role'] = 'student'
        return super().validate(attrs)

    def create(self, validated_data):
        student_number = self.generate_unique_student_number()
        validated_data['student_number'] = student_number

        if 'username' not in validated_data:
            full_name = validated_data.get('full_name', '')
            validated_data['username'] = full_name.replace(' ', '_').lower()

        return User.objects.create_user(**validated_data)

    def generate_unique_student_number(self):
        from django.utils.crypto import get_random_string

        while True:
            number = f"#{random.randint(10000, 99999)}"
            if not User.objects.filter(student_number=number).exists():
                return number


class FKJCreateSerializer(UserSerializer):
    class Meta:
        model = User
        fields = ['id', 'full_name', 'password', 'login_fkj', 'faculty', 'role']
        extra_kwargs = {
            'full_name': {'label': 'Полное имя'},
            'password': {'write_only': True, 'label': 'Пароль'},
            'faculty': {'label': 'Факультет'},
            'role': {'label': 'Роль'}
        }

    def validate(self, attrs):
        faculty = attrs.get('faculty')
        if not faculty:
            raise serializers.ValidationError({'faculty': 'Факультет обязателен для ФКЖ'})

        if User.objects.filter(faculty=faculty, role='fkj').exists():
            raise serializers.ValidationError({'faculty': 'Этот факультет уже привязан к другому ФКЖ'})

        attrs['role'] = 'fkj'
        return super().validate(attrs)



class AdminCreateSerializer(UserSerializer):
    class Meta:
        model = User
        fields = ['id', 'full_name', 'password', 'role']
        extra_kwargs = {
            'full_name': {'label': 'Полное имя'},
            'password': {'write_only': True, 'label': 'Пароль'},
            'role': {'label': 'Роль'}
        }

    def validate(self, attrs):
        attrs['role'] = 'admin'
        return super().validate(attrs)


class LoginLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', "full_name", 'ip_address', 'role', 'login_time']


class LoginSerializer(serializers.Serializer):
    login_fkj = serializers.CharField(required=False)
    username = serializers.CharField(required=False)
    password = serializers.CharField(required=False)
    full_name = serializers.CharField(required=False)
    course = serializers.IntegerField(required=False)

    def validate(self, data):
        # 🔐 Вход для ФКЖ (login_fkj + password)
        if 'login_fkj' in data and 'password' in data:
            try:
                user = User.objects.get(login_fkj=data['login_fkj'], role='fkj')
                if user.check_password(data['password']):
                    data['user'] = user
                    return data
            except User.DoesNotExist:
                pass
            raise serializers.ValidationError("Неверный логин или пароль для ФКЖ.")

        # 🔐 Вход для Админа (full_name + password)
        elif 'full_name' in data and 'password' in data:
            try:
                user = User.objects.get(full_name=data['full_name'], role='admin')
                if user.check_password(data['password']):
                    data['user'] = user
                    return data
            except User.DoesNotExist:
                pass
            raise serializers.ValidationError("Неверное имя или пароль для администратора.")

        # 🔐 Вход для Студента (full_name + course)
        elif 'full_name' in data and 'course' in data:
            try:
                user = User.objects.get(full_name=data['full_name'], course=data['course'], role='student')
                data['user'] = user
                return data
            except User.DoesNotExist:
                raise serializers.ValidationError("Неверные имя или курс для студента.")

        raise serializers.ValidationError("Недостаточно данных для входа.")