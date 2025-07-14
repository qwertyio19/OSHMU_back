from modeltranslation.translator import register, TranslationOptions
from apps.students.models import StudentProfile, DiaryEntry, SendingRaport, StudentCharacteristic

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

@register(SendingRaport)
class SendingRaportTranslationOptions(TranslationOptions):
    fields = (
        'title', 'tasks', 'dedline_tasks', 'raport_title', 'raport_text',
        'document_raport'
    )

@register(StudentCharacteristic)
class StudentCharacteristicTranslationOptions(TranslationOptions):
    fields = ('title_document',)