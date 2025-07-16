from rest_framework import serializers
from apps.students.models import StudentProfile, DiaryEntry, StudentCharacteristic, SendingReport, StudentTitles

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


class StudentTitlesSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentTitles
        fields = [
            'id', 'mini_title', 'mini_logo', 'logo',
            'title_document', 'title_documents', 'tasks', 'deadline', 'text_report',
            'document_report'
        ]
        read_only_fields = ['id']


class SendingReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = SendingReport
        fields = [
            'id', 'tasks',
            'report_text', 'link_report', 'file_report'
        ]
        read_only_fields = ['id']

    def validate_file_report(self, value):
        max_size_mb = 15
        if value.size > max_size_mb * 1024 * 1024:
            raise serializers.ValidationError(f"Файл слишком большой. Максимум {max_size_mb} МБ.")
        return value


class StudentCharacteristicSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentCharacteristic
        fields = [
            'id', 'student', 'title_document', 'title_filename'
        ]
        read_only_fields = ['id']
        