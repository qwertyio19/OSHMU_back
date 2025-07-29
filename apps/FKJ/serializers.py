from rest_framework import serializers
from apps.FKJ.models import Practice, TitlesFkj, Faculty, Speciality, Language
from apps.SuperAdmin.models import Institution
from apps.users.models import User


class ShortStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'full_name', 'course', 'student_number']


class PracticeSerializer(serializers.ModelSerializer):
    faculty = serializers.PrimaryKeyRelatedField(
        queryset=Faculty.objects.all(),
        label='Факультет'
    )
    speciality = serializers.PrimaryKeyRelatedField(
        queryset=Speciality.objects.all(),
        label='Специальность'
    )
    language = serializers.PrimaryKeyRelatedField(
        queryset=Language.objects.all(),
        label='Язык обучения'
    )
    institution = serializers.PrimaryKeyRelatedField(
        queryset=Institution.objects.all(),
        required=False,
        allow_null=True,
        label='Учреждения/Организация'
    )

    students = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.filter(role='student'),
        many=True,
        write_only=True,
        label='Студенты'
    )
    student_details = ShortStudentSerializer(source='students', many=True, read_only=True)
    work_days = serializers.MultipleChoiceField(
        choices=Practice.WEEKDAY_CHOICES,
        label="Дни практики",
        required=True, allow_blank=False
    )

    class Meta:
        model = Practice
        fields = [
            'id',
            'number',
            'course',
            'practice_type',
            'start_date',
            'end_date',
            'work_days',
            'start_time',
            'end_time',
            'faculty',
            'speciality',
            'institution',
            'language',
            'reception',
            'semester',
            'education_form',
            'students',
            'student_details',
        ]
  

class TitlesFkjSerializer(serializers.ModelSerializer):
    class Meta:
        model = TitlesFkj
        fields = [
            'id', 'period', 'working_days', 'opening_hours', 'type_of_practice', 'add_students', 'results', 'download_pdf', 'download_exel'
        ]
        read_only_fields = ['id']