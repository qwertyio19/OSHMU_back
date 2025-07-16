from django.contrib import admin
from apps.students.models import  StudentProfile, DiaryEntry, StudentCharacteristic, SendingReport, StudentTitles
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


class StudentTitlesAdmin(TranslationAdmin):
    fieldsets = (
        ("Русская версия", {
            'fields': ['mini_title_ru', 'title_document_ru', 'title_documents_ru', 'tasks_ru', 'deadline_ru', 'text_report_ru', 'document_report_ru']
        }),
        ("Кыргызская версия", {
            'fields': ['mini_title_ky', 'title_document_ky', 'title_documents_ky', 'tasks_ky', 'deadline_ky', 'text_report_ky', 'document_report_ky']
        }),
        ("Английская версия", {
            'fields': ['mini_title_en', 'title_document_en', 'title_documents_en', 'tasks_en', 'deadline_en', 'text_report_en', 'document_report_en']
        }),
        ("Общие данные", {
            'fields': ['logo', 'mini_logo'],
        }),
    )
   
admin.site.register(StudentTitles, StudentTitlesAdmin)


class SendingReportAdmin(TranslationAdmin):
    fieldsets = (
        ("Русская версия", {
            'fields': ['tasks_ru', 'report_text_ru']
        }),
        ("Кыргызская версия", {
            'fields': ['tasks_ky', 'report_text_ky']
        }),
        ("Английская версия", {
            'fields': ['tasks_en', 'report_text_en']
        }),
        ("Общие данные", {
            'fields': ['link_report', 'file_report',],
        }),
    )
   
admin.site.register(SendingReport, SendingReportAdmin)


class StudentCharacteristicAdmin(TranslationAdmin):
    fieldsets = (
        ("Русская версия", {'fields': ('title_document_ru',)}),
        ("Кыргызская версия", {'fields': ('title_document_ky',)}),
        ("Английская версия", {'fields': ('title_document_en',)}),
        ("Общие данные", {'fields': ('student', 'title_filename')}),
    )
   
admin.site.register(StudentCharacteristic, StudentCharacteristicAdmin)
