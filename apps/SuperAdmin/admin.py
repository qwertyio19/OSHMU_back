from django.contrib import admin
from apps.SuperAdmin.models import Institution, Faculty, Speciality
from django.utils.html import format_html
from .translations import *
from modeltranslation.admin import TranslationAdmin
from django.contrib import admin
from apps.SuperAdmin.models import Institution
from apps.SuperAdmin.translations import *
from django.utils.html import format_html




@admin.register(Institution)
class InstitutionAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Русская версия', {
            'fields': ['name_ru', 'type_ru', 'address_ru']
        }),
        ('Кыргызская версия', {
            'fields': ['name_ky', 'type_ky', 'address_ky']
        }),
        ('Англиская версия', {
            'fields': ['name_en', 'type_en', 'address_en']
        }),
        ('Глобальные', {
            'fields': ['logo', 'contact']
        })
    )


class FacultyAdmin(TranslationAdmin):
    fieldsets = (
        ('Русская версия', {
            'fields': ['faculty_ru'],
        }),
        ('Кыргызская версия', {
            'fields': ['faculty_ky'],
        }),
        ('Английская версия', {
            'fields': ['faculty_en'],
        }),
    )
admin.site.register(Faculty, FacultyAdmin)


class SpecialityAdmin(TranslationAdmin):
    fieldsets = (
        ('Русская версия', {
            'fields': ['speciality_ru'],
        }),
        ('Кыргызская версия', {
            'fields': ['speciality_ky'],
        }),
        ('Английская версия', {
            'fields': ['speciality_en'],
        }),
    )
admin.site.register(Speciality, SpecialityAdmin)


class DocumentAdmin(TranslationAdmin):
    fieldsets = (
        ("Русская версия", {'fields': ('title_ru', 'content_ru')}),
        ("Кыргызская версия", {'fields': ('title_ky', 'content_ky')}),
        ("Английская версия", {'fields': ('title_en', 'content_en')}),
    )
   
admin.site.register(Document, DocumentAdmin)