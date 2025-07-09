from django.db import models
from apps.users.models import User

class Institution(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='institutions',
        verbose_name='Пользователь',
    )
    logo = models.ImageField(
        upload_to='logos/',
        null=True, blank=True,
        verbose_name="Логотип учреждения",
        help_text='Загрузить логотип учреждения'
    )
    name = models.CharField(
        max_length=255,
        verbose_name='Название',
        help_text='Введите название учреждения/организации'
    )
    type = models.CharField(
        max_length=255,
        verbose_name='Тип',
        help_text='Введите тип учреждения/оригнизации'
    )
    contact = models.CharField(
        max_length=20,
        verbose_name='Контакт',
        help_text='Введите номер телефона учреждения/оригнизации'
    )
    address = models.TextField(
        verbose_name='Адрес',
        help_text='Введите адрес учреждения/оригнизации'
    )

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Создание учреждения"
        verbose_name_plural = "Создание учреждении"


class Course(models.Model):
    course = models.PositiveSmallIntegerField(verbose_name='Курсы', choices=[(1, '1 курс'), (2, '2 курс'), (3, '3 курс'), (4, '4 курс')])
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE, related_name='courses', verbose_name='Учиреждение')

    def __str__(self):
        return f'Курс {str(self.course)} - Учреждение {str(self.institution)}'
    
    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"

class Day(models.Model):
    day_number = models.PositiveSmallIntegerField(verbose_name='День', help_text='Номер дня в курсе')
    courses = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='days', verbose_name='Курс')

    def __str__(self):
        return f"День {str(self.day_number)} - Курс {str(self.courses.course)}"
    
    class Meta:
        verbose_name = "День"
        verbose_name_plural = "Дни"

class Task(models.Model):
    description = models.TextField(verbose_name='Введите задание')
    day = models.ForeignKey(Day, on_delete=models.CASCADE, related_name='tasks', verbose_name='День')
    order = models.IntegerField(default=0, verbose_name='Порядковый номер задачи')

    class Meta:
        verbose_name = "Задание"
        verbose_name_plural = "задания"
        ordering = ['order']

    def __str__(self):
        return f"Задача для {self.day} - {self.description[:20]}..."