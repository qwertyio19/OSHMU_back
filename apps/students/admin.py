from django.contrib import admin
from apps.students.models import StudentProfile, DiaryEntry, StudentCharacteristic, PracticeInfo, Document

@admin.register(StudentProfile)
class StudentProfileAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'phone_number')

@admin.register(DiaryEntry)
class DiaryEntryAdmin(admin.ModelAdmin):
    list_display = ('student', 'date')

@admin.register(StudentCharacteristic)
class StudentCharacteristicAdmin(admin.ModelAdmin):
    list_display = ('student',)

@admin.register(PracticeInfo)
class PracticeInfoAdmin(admin.ModelAdmin):
    list_display = ('student', 'company_name', 'mentor_name')

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('title', 'student', 'created_at')
