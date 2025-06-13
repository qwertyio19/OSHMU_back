from django.contrib import admin
from apps.SuperAdmin.models import Institution, Task, Course, Day
from django.utils.html import format_html
# Register your models here.

@admin.register(Institution)
class InstitutionAdmin(admin.ModelAdmin):
    list_display = ('id', 'display_logo', 'name', 'type', 'contact', 'address')
    
    def display_logo(self, obj):
        if obj.logo:  # предполагая, что поле называется 'logo' и это ImageField
            return format_html('<img src="{}" width="50" height="50" />', obj.logo.url)
        return "Нет логотипа"
    
    display_logo.short_description = 'Logo'

admin.site.register(Course)
admin.site.register(Day)
admin.site.register(Task)