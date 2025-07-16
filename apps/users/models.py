from django.db import models
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    username = models.CharField(
        max_length=150,
        unique=True,
        null=True,
        blank=True,
        verbose_name="Имя пользователя"
    )
    full_name = models.CharField(verbose_name="Полное имя", max_length=255, unique=True)
    faculty = models.ForeignKey('SuperAdmin.Faculty', on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Факультет")
    role = models.CharField(max_length=20, choices=[('student', 'Студент'), ('fkj', 'ФКЖ'), ('admin', 'Суперадмин')], default='student', verbose_name="Роль")
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
    speciality = models.ForeignKey('SuperAdmin.Speciality', on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Специальность")
    institution = models.ForeignKey('SuperAdmin.Institution', on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Учреждение")

    USERNAME_FIELD = 'full_name'
    REQUIRED_FIELDS = []

    def save(self, *args, **kwargs):
        if not self.username:
            self.username = self.full_name.replace(' ', '_').lower()
        super().save(*args, **kwargs)
    
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'



class LoginLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255, verbose_name="Имя пользователя", blank=True, null=True)
    ip_address = models.GenericIPAddressField(verbose_name="IP адрес", blank=True, null=True)
    role = models.CharField(max_length=20, verbose_name="Роль пользователя", blank=True, null=True)
    login_time = models.DateTimeField(auto_now_add=True, verbose_name="Время входа")

    def __str__(self):
        return f"{self.user.username} вошёл в {self.login_time}"
    

    class Meta:
        verbose_name = 'Журнал входа'
        verbose_name_plural = 'Журналы входа'
        ordering = ['-login_time']



# python manage.py shell

# from django.contrib.auth import get_user_model
# User = get_user_model()

# user = User.objects.create_superuser(
#     username='1',
#     full_name='1',
#     password='1',
#     role='admin'
# )