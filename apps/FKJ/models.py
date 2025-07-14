from django.db import models
from apps.users.models import User
from multiselectfield import MultiSelectField
from apps.SuperAdmin.models import Faculty, Speciality
from apps.students.models import StudentProfile



class Practice(models.Model):
    WEEKDAY_CHOICES = [
        ('Mon', 'Понедельник'),
        ('Tue', 'Вторник'),
        ('Wed', 'Среда'),
        ('Thu', 'Четверг'),
        ('Fri', 'Пятница'),
        ('Sat', 'Суббота'),
        ('Sun', 'Воскресенье'),
    ]

    PRACTICE_TYPES = [
        ('Introductory', 'Ознакомительная'),
        ('Professionally_Oriented', 'Профессионально-профильная'),
        ('Pre_Qualification', 'Предквалификационная'),
    ]

    RECEPTION = [
        ('Winter', 'Зимний'),
        ('Autumn', 'Осенний'),
    ]

    EDUCATION_FORMS = [
        ('Full_Time', 'Очная'),
        ('Part_Time', 'Заочная'),
        ('Blended', 'Очно-заочная'),
    ]

    SEMESTER = [
        ('Autumn', 'Осенний'),
        ('Spring', 'Весенний'),
    ]

    practice_type = models.CharField(max_length=30, choices=PRACTICE_TYPES, verbose_name="Тип практики")
    work_days = MultiSelectField(choices=WEEKDAY_CHOICES, verbose_name="Дни практики",)
    reception = models.CharField(max_length=20, choices=RECEPTION, verbose_name="Приём")
    semester = models.CharField(max_length=20, choices=SEMESTER, verbose_name="Семестр")
    education_form = models.CharField(max_length=20, choices=EDUCATION_FORMS, verbose_name="Форма обучения")
    start_date = models.DateField(verbose_name="Дата начала практики")
    end_date = models.DateField(verbose_name="Дата окончания практики")
    start_time = models.TimeField(verbose_name="Время начала практики")
    end_time = models.TimeField(verbose_name="Время окончания практики")

    faculty = models.ForeignKey(
        Faculty,
        on_delete=models.SET_NULL,
        null=True,
        related_name='practices',
        verbose_name='Факультет'
    )

    speciality = models.ForeignKey(
        Speciality,
        on_delete=models.SET_NULL,
        null=True,
        related_name='specialty_practices',
        verbose_name='Специальность'
    )

    students = models.ManyToManyField(
        StudentProfile,
        verbose_name='Студенты',
        related_name='practices',
        blank=True
    )

    def __str__(self):
        return f"{self.get_practice_type_display()} практика с {self.start_date.strftime('%d.%m.%Y')}"

    class Meta:
        verbose_name = "Создание практики"
        verbose_name_plural = "Создание практик"
