from django.contrib import admin
from apps.FKJ.models import Practice
from .translations import *
from modeltranslation.admin import TranslationAdmin




class PracticeAdmin(TranslationAdmin):
    fieldsets = (
        ('Русская версия', {
            'fields': ['practice_type_ru', 'work_days_ru', 'start_date_ru', 'end_date_ru', 'start_time_ru', 'end_time_ru', 'reception_ru', 'semester_ru', 'education_form_ru', 'faculty_ru', 'speciality_ru'],
        }),
        ('Кыргызская версия', {
            'fields': ['practice_type_ky', 'work_days_ky', 'start_date_ky', 'end_date_ky', 'start_time_ky', 'end_time_ky', 'reception_ky', 'semester_ky', 'education_form_ky', 'faculty_ky', 'speciality_ky'],
        }),
        ('Английская версия', {
            'fields': ['practice_type_en', 'work_days_en', 'start_date_en', 'end_date_en', 'start_time_en', 'end_time_en', 'reception_en', 'semester_en', 'education_form_en', 'faculty_en', 'speciality_en'],
        }),
    )
admin.site.register(Practice, PracticeAdmin)