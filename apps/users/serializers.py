from rest_framework import serializers
from rest_framework import serializers
from apps.users.models import User



# class UserSerializer(serializers.ModelSerializer):
#     password = serializers.CharField(write_only=True, label="Пароль")

#     class Meta:
#         model = User
#         fields = ['id', 'username', 'full_name', 'faculty', 'password', 'role']

#     def validate(self, attrs):
#         role = attrs.get("role")
#         faculty = attrs.get("faculty")

#         if role == "fkj" and faculty is None:
#             raise serializers.ValidationError({
#                 "faculty": "ФКЖ должен быть прикреплён к факультету."
#             })

#         return attrs

#     def create(self, validated_data):
#         password = validated_data.pop("password")
#         user = User(**validated_data)
#         user.set_password(password)
#         user.save()
#         return user

#     def to_representation(self, instance):
#         """Переопределим вывод, чтобы не показывать faculty=null для не-ФКЖ"""
#         rep = super().to_representation(instance)

#         # Удаляем faculty, если он null и роль не fkj
#         if instance.role != "fkj" and instance.faculty is None:
#             rep.pop("faculty", None)

#         return rep


# class BaseUserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['id', 'full_name', 'password', 'faculty', 'role']
#         extra_kwargs = {
#             'password': {'write_only': True}
#         }

#     def create(self, validated_data):
#         if 'username' not in validated_data:
#             full_name = validated_data.get('full_name', '')
#             username = full_name.replace(' ', '_').lower()
#             validated_data['username'] = username

#         return User.objects.create_user(**validated_data)

# class StudentCreateSerializer(BaseUserSerializer):
#     class Meta:
#         model = User
#         fields = ['id', 'full_name', 'password', 'role']
#         extra_kwargs = {
#             'password': {'write_only': True}
#         }

#     def validate(self, attrs):
#         attrs['role'] = 'student'
#         return super().validate(attrs)

# class FKJCreateSerializer(BaseUserSerializer):
#     class Meta:
#         model = User
#         fields = ['id', 'full_name', 'password', 'faculty', 'role']
#         extra_kwargs = {
#             'password': {'write_only': True}
#         }

#     def validate(self, attrs):
#         if not attrs.get('faculty'):
#             raise serializers.ValidationError({'faculty': 'Факультет обязателен для ФКЖ'})
#         attrs['role'] = 'fkj'
#         return super().validate(attrs)

# class AdminCreateSerializer(BaseUserSerializer):
#     class Meta:
#         model = User
#         fields = ['id', 'full_name', 'password', 'role']
#         extra_kwargs = {
#             'password': {'write_only': True}
#         }

#     def validate(self, attrs):
#         attrs['role'] = 'admin'
#         return super().validate(attrs)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'full_name', 'password', 'course', 'faculty', 'role']
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
        fields = ['id', 'full_name', 'password', 'course', 'role']
        extra_kwargs = {
            'full_name': {'label': 'Полное имя'},
            'password': {'write_only': True, 'label': 'Пароль'},
            'role': {'label': 'Роль'}
        }

    def validate(self, attrs):
        attrs['role'] = 'student'
        return super().validate(attrs)


class FKJCreateSerializer(UserSerializer):
    class Meta:
        model = User
        fields = ['id', 'full_name', 'password', 'faculty', 'role']
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

        # 🔍 Проверка: уже есть пользователь с этим факультетом и ролью "fkj"
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
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)