from django.db import models
from apps.users.models import User
from ckeditor.fields import RichTextField



class StudentProfile(models.Model):

    full_name = models.CharField(max_length=255, verbose_name="ФИО")
    phone_number = models.CharField(max_length=20, verbose_name="Номер телефона")
    birth_date = models.DateField(null=True, blank=True, verbose_name="Дата рождения")

    hash_tag = models.CharField(max_length=255, blank=True, null=True, verbose_name='Хэштег студента')
    avatarka = models.FileField(upload_to='media/avatarka', verbose_name='avatarka_file')
    avatarka_url = models.URLField(verbose_name='avatarka_url')

    institution = models.CharField(max_length=255, blank=True, verbose_name="Учреждение")
    course = models.IntegerField(blank=True, null=True, verbose_name="Курс на котором учиться студент")
    special = models.CharField(max_length=255, blank=True, null=True, verbose_name='Специальность студента')

    practice_day = models.CharField(max_length=255, blank=True, verbose_name="День практики")
    practice_schedule = models.CharField(max_length=255, blank=True, verbose_name="Граффик практики")
    practice_raport = models.CharField(max_length=255, blank=True, verbose_name="Отчет о практики")

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = "Профиль студента"
        verbose_name_plural = "Профили студентов"



class DiaryEntry(models.Model):

    student = models.ForeignKey(StudentProfile ,on_delete=models.SET_NULL, related_name='diary', null=True, blank=True)
    date = models.CharField(max_length=255, blank=True, null=True, verbose_name="дата начала и конца")
    course = models.TextField(max_length=255, blank=True, null=True, verbose_name="курс студента")
    organization = models.TextField(max_length=255, blank=True, null=True, verbose_name='организация - учреждение')

    title_behind = models.TextField(max_length=255, blank=True, null=True, verbose_name='Заголовок внутри')
    date_behind = models.CharField(max_length=255, blank=True, null=True, verbose_name='Дата внутри')
    number_behind = models.IntegerField(blank=True, null=True, verbose_name='Нумерация')

    def __str__(self):
        student_name = self.student.full_name if self.student else "Неизвестный студент"
        return f"Дневник {self.date} — {student_name}"

    class Meta:
        verbose_name = "Дневник"
        verbose_name_plural = "Дневники"
        ordering = ['-date']



class SendingRaport(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True, verbose_name='Заголовок задачи')
    tasks = RichTextField(blank=True, null=True, verbose_name='Задачи:')
    dedline_tasks = models.CharField(max_length=255, blank=True, null=True, verbose_name='Дедлайн задачи')

    raport_title = models.CharField(max_length=255, blank=True, null=True, verbose_name='Заголовок отчета')
    raport_text = RichTextField(blank=True, null=True, verbose_name='Текст отчета')

    document_raport = models.URLField(verbose_name='Ссылка на документ отчета')
    file_raport = models.FileField(upload_to='media/files/', verbose_name='файл_отчета')

    def __str__(self):
        return self.title or "Отчет без названия"

    class Meta:
        verbose_name = "Отправка отчёта"
        verbose_name_plural = "Отправка отчётов"


class StudentCharacteristic(models.Model):
    student = models.OneToOneField(StudentProfile, on_delete=models.SET_NULL, null=True, blank=True)

    title_document = models.CharField(max_length=255, blank=True, verbose_name="Заголовок Документы")
    title_filename = models.FileField(upload_to='media/characteristik', blank=True, null=True, verbose_name="Файл документа характеристики")

    def __str__(self):
        student_name = self.student.full_name if self.student else "Неизвестный студент"
        return f"Характеристика - {student_name}"

    class Meta:
        verbose_name = "Характеристика студента"
        verbose_name_plural = "Характеристики студентов"