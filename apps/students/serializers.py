from rest_framework import serializers
from apps.students.models import StudentProfile
from rest_framework import serializers
from apps.students.models import StudentProfile, Document, DiaryEntry, StudentCharacteristic, PracticeInfo

class StudentProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentProfile
        fields = ['id', 'full_name', 'course', 'birth_date', 'phone_number']
        read_only_fields = ['id']

class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ['id', 'title', 'content', 'created_at']
        read_only_fields = ['id', 'created_at']

class DiaryEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = DiaryEntry
        fields = ['id', 'date', 'entry']
        read_only_fields = ['id']

class StudentCharacteristicSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentCharacteristic
        fields = ['id', 'strengths', 'weaknesses', 'notes']
        read_only_fields = ['id']

class PracticeInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PracticeInfo
        fields = ['id', 'company_name', 'mentor_name', 'start_date', 'end_date', 'description']
        read_only_fields = ['id']