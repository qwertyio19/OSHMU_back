from rest_framework import serializers
from apps.FKJ.models import Practice, TitlesFkj, Faculty, Speciality
from apps.students.models import StudentProfile



class PracticeSerializer(serializers.ModelSerializer):
    faculty = serializers.PrimaryKeyRelatedField(
        queryset=Faculty.objects.all(),
        label='Факультет'
    )
    speciality = serializers.PrimaryKeyRelatedField(
        queryset=Speciality.objects.all(),
        label='Специальность'
    )
    students = serializers.PrimaryKeyRelatedField(
        queryset=StudentProfile.objects.all(),
        many=True, label='Студенты'
    )
    work_days = serializers.MultipleChoiceField(
        choices=Practice.WEEKDAY_CHOICES,
        label="Дни практики"
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
            'reception',
            'semester',
            'education_form',
            'students',
        ]
  

class TitlesFkjSerializer(serializers.ModelSerializer):
    class Meta:
        model = TitlesFkj
        fields = [
            'id', 'period', 'working_days', 'opening_hours', 'type_of_practice', 'add_students', 'results', 'download_pdf', 'download_exel'
        ]
        read_only_fields = ['id']