from modeltranslation.translator import register, TranslationOptions
from apps.FKJ.models import Practice


@register(Practice)
class PracticeTranslation(TranslationOptions):
    fields = (
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
