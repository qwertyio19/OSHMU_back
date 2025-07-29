from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User
from .forms import UserAdminCreationForm

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    add_form = UserAdminCreationForm
    model = User

    # ✅ Что отображается в списке
    list_display = ('id', 'full_name', 'role', 'course', 'faculty', 'institution', 'student_number', 'is_active')
    
    # ✅ Фильтры справа
    list_filter = ('role', 'course', 'faculty', 'institution', 'is_active')

    # ✅ Поля, по которым работает поиск
    search_fields = ('full_name', 'student_number', 'username', 'email')

    # ✅ Сортировка
    ordering = ('id',)

    # ✅ Поля в отображении пользователя
    fieldsets = (
        (None, {'fields': ('full_name', 'password')}),
        ('Персональная информация', {
            'fields': ('username', 'email', 'role', 'course', 'faculty', 'speciality', 'institution', 'student_number')
        }),
        ('Права доступа', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
    )

    # ✅ Поля при создании нового пользователя
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('full_name', 'password', 'role', 'course', 'faculty', 'speciality', 'institution')}
        ),
    )
