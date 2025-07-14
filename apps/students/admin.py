from django.contrib import admin
from apps.students.models import  StudentProfile, DiaryEntry, StudentCharacteristic, SendingRaport
from modeltranslation.admin import TranslationAdmin
from apps.students.translations import *


class StudentProfileAdmin(TranslationAdmin):
    fieldsets = (
        ("Русская версия", {
            'fields': (
                'full_name_ru', 'phone_number_ru', 'hash_tag_ru', 'institution_ru', 
                'special_ru', 'practice_day_ru', 'practice_schedule_ru', 'practice_raport_ru',
            )
        }),
        ("Кыргызская версия", {
            'fields': (
                'full_name_ky', 'phone_number_ky', 'hash_tag_ky', 'institution_ky', 
                'special_ky', 'practice_day_ky', 'practice_schedule_ky', 'practice_raport_ky',
            )
        }),
        ("Английская версия", {
            'fields': (
                'full_name_en', 'phone_number_en', 'hash_tag_en', 'institution_en', 
                'special_en', 'practice_day_en', 'practice_schedule_en', 'practice_raport_en',
            )
        }),
        ("Общие данные", {
            'fields': ('birth_date', 'avatarka', 'course'),
        }),
    )
admin.site.register(StudentProfile, StudentProfileAdmin)


class DiaryEntryAdmin(TranslationAdmin):
    fieldsets = (
        ("Русская версия", {'fields': ('date_ru', 'course_ru', 'organization_ru', 'title_behind_ru', 'date_behind_ru')}),
        ("Кыргызская версия", {'fields': ('date_ky', 'course_ky', 'organization_ky', 'title_behind_ky', 'date_behind_ky')}),
        ("Английская версия", {'fields': ('date_en', 'course_en', 'organization_en', 'title_behind_en', 'date_behind_en')}),
        ("Общие данные", {'fields': ('student', 'number_behind')}),
    )
  
admin.site.register(DiaryEntry, DiaryEntryAdmin)


class SendingRaportAdmin(TranslationAdmin):
    fieldsets = (
        ("Русская версия", {
            'fields': ['title_ru', 'tasks_ru', 'dedline_tasks_ru', 'raport_title_ru', 'raport_text_ru', 'document_raport_ru']
        }),
        ("Кыргызская версия", {
            'fields': ['title_ky', 'tasks_ky', 'dedline_tasks_ky', 'raport_title_ky', 'raport_text_ky', 'document_raport_ky']
        }),
        ("Английская версия", {
            'fields': ['title_en', 'tasks_en', 'dedline_tasks_en', 'raport_title_en', 'raport_text_en', 'document_raport_en']
        }),
        ("Общие данные", {
            'fields': ['file_raport',],
        }),
    )
   
admin.site.register(SendingRaport, SendingRaportAdmin)


class StudentCharacteristicAdmin(TranslationAdmin):
    fieldsets = (
        ("Русская версия", {'fields': ('title_document_ru',)}),
        ("Кыргызская версия", {'fields': ('title_document_ky',)}),
        ("Английская версия", {'fields': ('title_document_en',)}),
        ("Общие данные", {'fields': ('student', 'title_filename')}),
    )
   
admin.site.register(StudentCharacteristic, StudentCharacteristicAdmin)
