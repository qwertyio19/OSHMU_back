from rest_framework import serializers
from apps.students.models import StudentProfile, DiaryEntry, StudentCharacteristic, SendingRaport

class StudentProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentProfile
        fields = [
            'id', 'full_name', 'phone_number', 'birth_date',
            'hash_tag', 'avatarka', 'institution', 'course', 'special',
            'practice_day', 'practice_schedule', 'practice_raport', 'avatarka_url'
        ]
        read_only_fields = ['id']



class DiaryEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = DiaryEntry
        fields = [
            'id', 'student', 'date', 'course', 'organization',
            'title_behind', 'date_behind', 'number_behind'
        ]
        read_only_fields = ['id']


class SendingRaportSerializer(serializers.ModelSerializer):
    class Meta:
        model = SendingRaport
        fields = [
            'id', 'title', 'tasks', 'dedline_tasks',
            'raport_title', 'raport_text', 'document_raport', 'file_raport'
        ]
        read_only_fields = ['id']


class StudentCharacteristicSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentCharacteristic
        fields = [
            'id', 'student', 'title_document', 'title_filename'
        ]
        read_only_fields = ['id']
        