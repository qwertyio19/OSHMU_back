from modeltranslation.translator import register, TranslationOptions
from apps.SuperAdmin.models import Faculty, Speciality, Document, Institution


@register(Institution)
class InstitutionTranslationOptions(TranslationOptions):
    fields = ('name', 'type', 'address')

@register(Faculty)
class FacultyTranslation(TranslationOptions):
    fields = ("faculty",)

@register(Speciality)
class SpecialityTranslation(TranslationOptions):
    fields = ("speciality",)

@register(Document)
class DocumentTranslationOptions(TranslationOptions):
    fields = ('title', 'content')