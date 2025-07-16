from modeltranslation.translator import register, TranslationOptions
from apps.FKJ.models import Practice, TitlesFkj


@register(Practice)
class PracticeTranslation(TranslationOptions):
    fields = (
        'number',
        'practice_type',
        'start_date',
        'end_date',
        'work_days',
        'start_time',
        'end_time',
        'reception',
        'semester',
        'education_form',
        'faculty',
        'speciality',
    )

@register(TitlesFkj)
class TitlesFkjTranslation(TranslationOptions):
    fields = ('period', 'working_days', 'opening_hours', 'type_of_practice', 'add_students', 'results', 'download_pdf', 'download_exel')