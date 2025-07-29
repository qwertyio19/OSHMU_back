from django.contrib import admin
from apps.SuperAdmin.models import Institution, Faculty, Speciality, TitlesAdmin, Document, Language
from .translations import *
from modeltranslation.admin import TranslationAdmin
from apps.SuperAdmin.translations import *



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
            'fields': ['logo', 'contact', 'fkj']
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


class LanguageAdmin(TranslationAdmin):
    fieldsets = (
        ('Русская версия', {
            'fields': ['language_ru'],
        }),
        ('Кыргызская версия', {
            'fields': ['language_ky'],
        }),
        ('Английская версия', {
            'fields': ['language_en'],
        }),
    )
admin.site.register(Language, LanguageAdmin)


class DocumentAdmin(TranslationAdmin):
    fieldsets = (
        ("Русская версия", {'fields': ('title_ru', 'content_ru')}),
        ("Кыргызская версия", {'fields': ('title_ky', 'content_ky')}),
        ("Английская версия", {'fields': ('title_en', 'content_en')}),
    )
admin.site.register(Document, DocumentAdmin)


class TitlesAdminAdmin(TranslationAdmin):
    fieldsets = (
        ('Русская версия', {
            'fields': ['full_name_ru', 'faculty_ru', 'institution_ru', 'type_institution_ru', 'address_ru',
                       'phone_number_ru', 'students_ru', 'institution_organization_ru', 'course_ru', 'metodist_ru',
                       'period_ru', 'name_ru', 'type_ru', 'contacts_ru', 'full_name_fkj_ru', 'login_ru', 'password_ru'],
        }),
        ('Кыргызская версия', {
            'fields': ['full_name_ky', 'faculty_ky', 'institution_ky', 'type_institution_ky', 'address_ky',
                       'phone_number_ky', 'students_ky', 'institution_organization_ky', 'course_ky', 'metodist_ky',
                       'period_ky', 'name_ky', 'type_ky', 'contacts_ky', 'full_name_fkj_ky', 'login_ky', 'password_ky'],
        }),
        ('Английская версия', {
            'fields': ['full_name_en', 'faculty_en', 'institution_en', 'type_institution_en', 'address_en',
                       'phone_number_en', 'students_en', 'institution_organization_en', 'course_en', 'metodist_en',
                       'period_en', 'name_en', 'type_en', 'contacts_en', 'full_name_fkj_en', 'login_en', 'password_en'],
        }),
    )
admin.site.register(TitlesAdmin, TitlesAdminAdmin)