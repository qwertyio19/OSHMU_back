from django.db import models
from apps.users.models import User
from ckeditor.fields import RichTextField


class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="student_profile")
    full_name = models.CharField(max_length=255, verbose_name="ФИО")
    phone_number = models.CharField(max_length=20, verbose_name="Номер телефона")
    birth_date = models.DateField(null=True, blank=True, verbose_name="Дата рождения")
    institution = models.CharField(max_length=255, blank=True, verbose_name="Учреждение")

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = "Профиль студента"
        verbose_name_plural = "Профили студентов"


class Document(models.Model):
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE, related_name='documents')
    title = models.CharField(max_length=255)
    content = RichTextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Документ студента"
        verbose_name_plural = "Документы студентов"


class DiaryEntry(models.Model):
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE, related_name='diary')
    date = models.DateField()
    entry = models.TextField()

    def __str__(self):
        return f"Дневник {self.date} — {self.student.full_name}"

    class Meta:
        verbose_name = "Запись дневника"
        verbose_name_plural = "Записи дневника"
        ordering = ['-date']


class StudentCharacteristic(models.Model):
    student = models.OneToOneField(StudentProfile, on_delete=models.CASCADE)
    strengths = models.TextField()
    weaknesses = models.TextField()
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"Характеристика - {self.student.full_name}"

    class Meta:
        verbose_name = "Характеристика студента"
        verbose_name_plural = "Характеристики студентов"


class PracticeInfo(models.Model):
    student = models.OneToOneField(StudentProfile, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=255)
    mentor_name = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    description = RichTextField()

    def __str__(self):
        return f"Практика — {self.student.full_name}"

    class Meta:
        verbose_name = "Информация о практике"
        verbose_name_plural = "Информация о практиках"