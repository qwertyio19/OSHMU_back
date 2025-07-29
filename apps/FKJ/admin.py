from django.contrib import admin
from apps.FKJ.models import Practice, TitlesFkj
from .translations import *
from modeltranslation.admin import TranslationAdmin



class PracticeAdmin(TranslationAdmin):
    fieldsets = (
        ('Русская версия', {
            'fields': ['number_ru', 'practice_type_ru', 'work_days_ru', 'start_date_ru', 'end_date_ru', 'start_time_ru', 'end_time_ru', 'reception_ru', 'semester_ru', 'education_form_ru', 'faculty_ru', 'speciality_ru'],
        }),
        ('Кыргызская версия', {
            'fields': ['number_ky', 'practice_type_ky', 'work_days_ky', 'start_date_ky', 'end_date_ky', 'start_time_ky', 'end_time_ky', 'reception_ky', 'semester_ky', 'education_form_ky', 'faculty_ky', 'speciality_ky'],
        }),
        ('Английская версия', {
            'fields': ['number_en', 'practice_type_en', 'work_days_en', 'start_date_en', 'end_date_en', 'start_time_en', 'end_time_en', 'reception_en', 'semester_en', 'education_form_en', 'faculty_en', 'speciality_en'],
        }),
        ("Курс / Студенты", {
            'fields': ('course', 'students', 'institution', 'language'),
        }),
    )
admin.site.register(Practice, PracticeAdmin)


class TitlesFkjAdmin(TranslationAdmin):
    fieldsets = (
        ('Русская версия', {
            'fields': ['period_ru', 'working_days_ru', 'opening_hours_ru', 'type_of_practice_ru', 'add_students_ru', 'results_ru', 'download_pdf_ru', 'download_exel_ru'],
        }),
        ('Кыргызская версия', {
            'fields': ['period_ky', 'working_days_ky', 'opening_hours_ky', 'type_of_practice_ky', 'add_students_ky', 'results_ky', 'download_pdf_ky', 'download_exel_ky'],
        }),
        ('Английская версия', {
            'fields': ['period_en', 'working_days_en', 'opening_hours_en', 'type_of_practice_en', 'add_students_en', 'results_en', 'download_pdf_en', 'download_exel_en'],
        }),
    )
admin.site.register(TitlesFkj, TitlesFkjAdmin)