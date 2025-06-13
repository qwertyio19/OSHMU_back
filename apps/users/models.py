from django.db import models
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField


class User(AbstractUser):

    class Role(models.TextChoices):
        STUDENT = "student", "Студент"
        FKZH = "fkzh", "ФКЖ"
        ADMIN = "admin", "Админ"

    role = models.CharField(
        max_length=20,
        choices=Role.choices,
        default=Role.STUDENT,
        verbose_name='Роль пользователя')

    def __str__(self):
        return self.role
    
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'