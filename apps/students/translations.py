from modeltranslation.translator import register, TranslationOptions
from apps.students.models import SendingReport, StudentTitles



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