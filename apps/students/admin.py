from django.contrib import admin
from apps.students.models import SendingReport, StudentTitles, Characteristics
from modeltranslation.admin import TranslationAdmin
from apps.students.translations import *


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
            'fields': ['link_report', 'practice', 'file_report', 'file_report_2', 'file_report_3', 'file_report_4'],
        }),
    )
   
admin.site.register(SendingReport, SendingReportAdmin)

admin.site.register(Characteristics)