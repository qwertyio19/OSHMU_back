from modeltranslation.translator import register, TranslationOptions
from apps.students.models import StudentProfile, DiaryEntry, SendingReport, StudentCharacteristic, StudentTitles

@register(StudentProfile)
class StudentProfileTranslationOptions(TranslationOptions):
    fields = (
        'full_name', 'phone_number', 'hash_tag', 'institution', 
        'special', 'practice_day', 'practice_schedule', 'practice_raport'
    )


@register(DiaryEntry)
class DiaryEntryTranslationOptions(TranslationOptions):
    fields = (
        'date', 'course', 'organization', 'title_behind', 'date_behind',
    )


@register(StudentTitles)
class StudentTitlesTranslationOptions(TranslationOptions):
    fields = (
        'mini_title', 'title_document', 'title_documents', 'tasks',
        'deadline', 'text_report', 'document_report'
    )

@register(SendingReport)
class SendingRaportTranslationOptions(TranslationOptions):
    fields = (
        'tasks', 'report_text'
    )

@register(StudentCharacteristic)
class StudentCharacteristicTranslationOptions(TranslationOptions):
    fields = ('title_document',)