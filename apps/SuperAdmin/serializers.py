from rest_framework import serializers
from apps.SuperAdmin.models import Institution, Course, Day, Task
import re

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'description', 'day', 'order']

class DaySerializer(serializers.ModelSerializer):
    tasks = TaskSerializer(many=True, read_only=True)
    
    class Meta:
        model = Day
        fields = ['id', 'day_number', 'courses', 'tasks']

class CourseSerializer(serializers.ModelSerializer):
    days = DaySerializer(many=True, read_only=True)
    
    class Meta:
        model = Course
        fields = ['id', 'course', 'institution', 'days']
        
class InstitutionSerializer(serializers.ModelSerializer):
    class Meta:
        courses = CourseSerializer(many=True, read_only=True)


        model = Institution
        fields = ["id", "logo", "name", 'type', 'contact', 'address']

    def validate(self, attrs):
        
        contact = attrs['contact'].replace(" ", "").strip()

        if not contact.startswith('+996'):
            raise serializers.ValidationError({'contact': 'Номер должен начинаться с +996'})

        contact_pattern = r'^\+996\d{9}$'
        if not re.fullmatch(contact_pattern, contact):
            raise serializers.ValidationError({'contact': 'Некорректный номер. Формат: +996XXXXXXXXX'})

        attrs['contact'] = contact
        return attrs
    
    def create(self, values):
        institution = Institution.objects.create(
            logo=values['logo'],
            name=values['name'],
            type=values['type'],
            contact=values['contact'],
            address=values['address'],
        )
        institution.save()
        return institution

