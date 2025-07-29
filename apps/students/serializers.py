from rest_framework import serializers
from apps.students.models import SendingReport, StudentTitles, Characteristics
from apps.users.models import User



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
            'id', 'practice', 'tasks',
            'report_text', 'link_report', 'file_report', 'file_report_2', 'file_report_3', 'file_report_4'
        ]
        read_only_fields = ['id']

        extra_kwargs = {
            'file_report': {'required': False, 'allow_null': True},
            'file_report_2': {'required': False, 'allow_null': True},
            'file_report_3': {'required': False, 'allow_null': True},
            'file_report_4': {'required': False, 'allow_null': True},
            }

    def validate_file_report(self, value):
        if value:
            max_size_mb = 15
            if value.size > max_size_mb * 1024 * 1024:
                raise serializers.ValidationError(f"Файл слишком большой. Максимум {max_size_mb} МБ.")
        return value

    def validate(self, attrs):
        user = self.context['request'].user
        practice = attrs.get('practice')

        if not user.role == 'student':
            raise serializers.ValidationError("Только студент может отправлять отчёт.")

        if not practice.students.filter(id=user.id).exists():
            raise serializers.ValidationError("Вы не прикреплены к этой практике.")

        return attrs

    def create(self, validated_data):
        validated_data['student'] = self.context['request'].user
        return super().create(validated_data)



class StudentProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'full_name', 'student_number', 'course', 'institution', 'speciality']



class CharacteristicsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Characteristics
        fields = ['id', 'file']

    def validate_file(self, value):
        max_size_mb = 15
        if value.size > max_size_mb * 1024 * 1024:
            raise serializers.ValidationError(f"Файл слишком большой. Максимум {max_size_mb} МБ.")
        return value