from rest_framework import serializers
from .models import Institution, Course, Day, Task
import re

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'description', 'day', 'order']
        read_only_fields = ['id']  # ID только для чтения

class DaySerializer(serializers.ModelSerializer):
    tasks = TaskSerializer(many=True, read_only=True)
    
    class Meta:
        model = Day
        fields = ['id', 'day_number', 'courses', 'tasks']
        read_only_fields = ['id']

class CourseSerializer(serializers.ModelSerializer):
    days = DaySerializer(many=True, read_only=True)
    
    class Meta:
        model = Course
        fields = ['id', 'course', 'institution', 'days']
        read_only_fields = ['id']
        
class InstitutionSerializer(serializers.ModelSerializer):
    courses = CourseSerializer(many=True, read_only=True)  # Исправлено: было class Meta внутри

    class Meta:
        model = Institution
        fields = ["id", "logo", "name", "type", "contact", "address", "courses", 'user']
        read_only_fields = ['id', 'courses', 'user']

    def validate_contact(self, value):
        contact = value.replace(" ", "").strip()

        if not contact.startswith('+996'):
            raise serializers.ValidationError('Номер должен начинаться с +996')

        contact_pattern = r'^\+996\d{9}$'
        if not re.fullmatch(contact_pattern, contact):
            raise serializers.ValidationError('Некорректный номер. Формат: +996XXXXXXXXX')

        return contact