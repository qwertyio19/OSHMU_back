from django.db import models
from django.forms import ValidationError
from apps.users.models import User
from ckeditor.fields import RichTextField


class StudentTitles(models.Model):
    mini_title = models.CharField(max_length=255, verbose_name='Мини заголовок')
    mini_logo = models.ImageField(upload_to='media/logo', verbose_name='Мини логотип')
    logo = models.ImageField(upload_to='media/logo', verbose_name='Логотип')
    title_document = models.CharField(max_length=255, verbose_name='Заголовок "Документ"', default='Документ')
    title_documents = models.CharField(max_length=255, verbose_name='Заголовок "Документы"', default='Документы')
    tasks = models.CharField(max_length=255, verbose_name='Заголовок "Задачи"', default='Задачи')
    deadline = models.CharField(max_length=255, verbose_name='Заголовок "Дедлайн"', default='Дедлайн')
    text_report = models.CharField(max_length=255, verbose_name='Заголовок "Текстовый отчет"', default='Текстовый отчет')
    document_report = models.URLField(verbose_name='Заголовок "Документальный отчет"', default='Документальный отчет')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Заголовок студента"
        verbose_name_plural = "Заголовки студентов"


class SendingReport(models.Model):
    student = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='reports', null=True, blank=True)
    practice = models.ForeignKey('FKJ.Practice', on_delete=models.SET_NULL, null=True, blank=True, related_name="student_practices")

    tasks = RichTextField(blank=True, null=True, verbose_name='Задача')
    report_text = RichTextField(blank=True, null=True, verbose_name='Текстовый отчет')

    link_report = models.URLField(verbose_name='Ссылка на документ отчета')
    file_report = models.FileField(upload_to='media/files/', blank=True, null=True, verbose_name='файл отчета')
    file_report_2 = models.FileField(upload_to='media/files/', blank=True, null=True, verbose_name='файл отчета')
    file_report_3 = models.FileField(upload_to='media/files/', blank=True, null=True, verbose_name='файл отчета')
    file_report_4 = models.FileField(upload_to='media/files/', blank=True, null=True, verbose_name='файл отчета')

    def clean(self):
        max_size_mb = 15
        max_size = max_size_mb * 1024 * 1024
        errors = {}

        for field_name in ['file_report', 'file_report_2', 'file_report_3', 'file_report_4']:
            file = getattr(self, field_name)
            if file and file.size > max_size:
                errors[field_name] = f'Файл слишком большой. Максимум {max_size_mb} МБ.'

        if errors:
            raise ValidationError(errors)

    def __str__(self):
        return self.tasks

    class Meta:
        verbose_name = "Отправка отчёта"
        verbose_name_plural = "Отправка отчётов"


class Characteristics(models.Model):
    file = models.FileField(upload_to='media/files/', verbose_name='Файл')

    def __str__(self):
        return str(self.file)
    
    def clean(self):
        max_size_mb = 15
        if self.file and self.file.size > max_size_mb * 1024 * 1024:
            raise ValidationError({'file': f'Файл слишком большой. Максимум {max_size_mb} МБ.'})
    
    class Meta:
        verbose_name = 'Характеристика'
        verbose_name_plural = 'Характеристики'