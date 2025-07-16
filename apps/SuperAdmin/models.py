import re
from django.db import models
from django.forms import ValidationError
from apps.users.models import User
from ckeditor.fields import RichTextField


class Institution(models.Model):

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

    def validate_phone_number(value):
        pattern = r'^\+996\d{9}$'
        if not re.match(pattern, value):
            raise ValidationError("Номер телефона должен быть в формате +996XXXXXXXXX")

    contact = models.CharField(
        max_length=20,
        verbose_name='Контакт', 
        validators=[validate_phone_number],
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
        verbose_name_plural = "Создание учреждений"
    


class Faculty(models.Model):
    faculty = models.CharField(
        max_length=255,
        verbose_name='Факультет')

    def __str__(self):
        return self.faculty
    
    class Meta:
        verbose_name = "Факультет"
        verbose_name_plural = "Факультеты"


class Speciality(models.Model):
    speciality = models.CharField(
        max_length=255,
        verbose_name='Специальность')

    def __str__(self):
        return self.speciality
    
    class Meta:
        verbose_name = "Специальность"
        verbose_name_plural = "Специальности"


class Document(models.Model):

    title = models.CharField(max_length=255, verbose_name='Заголовок документа')
    content = RichTextField(verbose_name='Содержание документа')

    def __str__(self):
        return self.title or "Документ без названия"

    class Meta:
        verbose_name = "Документ студента"
        verbose_name_plural = "Документы студентов"


class TitlesAdmin(models.Model):
    full_name = models.CharField(max_length=300, verbose_name='Заголовок "ФИО"', default='ФИО')
    faculty = models.CharField(max_length=300, verbose_name='Заголовок "Факультет"', default='Факультет')
    institution = models.CharField(max_length=300, verbose_name='Заголовок "Учреждение"', default='Учреждение')
    type_institution = models.CharField(max_length=300, verbose_name='Заголовок "Тип учреждения"', default='Тип учреждения')
    address = models.CharField(max_length=300, verbose_name='Заголовок "Адрес"', default='Адрес')
    phone_number = models.CharField(max_length=300, verbose_name='Заголовок "Телефон"', default='Телефон')
    students = models.CharField(max_length=300, verbose_name='Заголовок "Студенты"', default='Студенты')
    institution_organization = models.CharField(max_length=300, verbose_name='Заголовок "Учреждение/Организация"', default='Учреждение/Организация')
    course = models.CharField(max_length=300, verbose_name='Заголовок "Курс"', default='Курс')
    metodist = models.CharField(max_length=300, verbose_name='Заголовок "Методист"', default='Методист')
    period = models.CharField(max_length=300, verbose_name='Заголовок "Период"', default='Период')

    name = models.CharField(max_length=300, verbose_name='Заголовок "Название"', default='Название')
    type = models.CharField(max_length=300, verbose_name='Заголовок "Тип"', default='Тип')
    contacts = models.CharField(max_length=300, verbose_name='Заголовок "Контакты"', default='Контакты')

    full_name_fkj = models.CharField(max_length=300, verbose_name='Заголовок "Имя фамилия ФКЖ"', default='Имя фамилия ФКЖ')
    login = models.CharField(max_length=300, verbose_name='Заголовок "Логин"', default='Логин')
    password = models.CharField(max_length=300, verbose_name='Заголовок "Пароль"', default='Пароль')

    def __str__(self):
        return self.period

    class Meta:
        verbose_name = "Заголовок суперадмина"
        verbose_name_plural = "Заголовки суперадмина"