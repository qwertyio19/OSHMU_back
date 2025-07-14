from rest_framework import serializers
# from apps.FKJ.models import FKJUser
from apps.FKJ.models import Practice
from apps.FKJ.models import Faculty, Speciality
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
  