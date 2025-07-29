from django.db import models
from multiselectfield import MultiSelectField
from apps.SuperAdmin.models import Faculty, Speciality, Language



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

    course = models.PositiveSmallIntegerField(
        choices=[
            (1, '1 курс'),
            (2, '2 курс'),
            (3, '3 курс'),
            (4, '4 курс'),
            (5, '5 курс'),
            (6, '6 курс'),
            (7, '7 курс'),
        ],
        null=True, blank=True,
        verbose_name='Курс'
    )

    number = models.CharField(max_length=255, verbose_name="Номер практики")
    practice_type = models.CharField(max_length=30, choices=PRACTICE_TYPES, verbose_name="Тип практики")
    work_days = MultiSelectField(choices=WEEKDAY_CHOICES, verbose_name="Дни практики")
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

    language = models.ForeignKey(
        Language,
        on_delete=models.SET_NULL,
        null=True,
        related_name='language_lessons',
        verbose_name='Язык обучения'
    )

    students = models.ManyToManyField(
        'users.User',
        related_name='practices',
        limit_choices_to={'role': 'student'},
        verbose_name='Студенты'
    )

    institution = models.ForeignKey(
        'SuperAdmin.Institution',
        on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name='institution_practices',
        verbose_name='Учреждение'
    )

    def __str__(self):
        return f"{self.get_practice_type_display()} практика с {self.start_date.strftime('%d.%m.%Y')}"

    class Meta:
        verbose_name = "Создание практики"
        verbose_name_plural = "Создание практик"



class TitlesFkj(models.Model):
    period = models.CharField(max_length=255, verbose_name='Заголовок "Период:"', default='Период:')
    working_days = models.CharField(max_length=255, verbose_name='Заголовок "Рабочие дни:"', default='Рабочие дни:')
    opening_hours = models.CharField(max_length=255, verbose_name='Заголовок "Часы работы:"', default='Часы работы:')
    type_of_practice = models.CharField(max_length=255, verbose_name='Заголовок "Тип практики:"', default='Тип практики:')
    add_students = models.CharField(max_length=255, verbose_name='Заголовок "Добавить студентов:"', default='Добавить студентов:')
    results = models.CharField(max_length=255, verbose_name='Заголовок "Результаты:"', default='Результаты:')
    download_pdf = models.CharField(max_length=255, verbose_name='Заголовок "Скачать PDF"', default='Скачать PDF')
    download_exel = models.CharField(max_length=255, verbose_name='Заголовок "Скачать Excel"', default='Скачать Excel')

    def __str__(self):
        return self.mini_title

    class Meta:
        verbose_name = 'Заголовки ФКЖ'
        verbose_name_plural = 'Заголовки ФКЖ'