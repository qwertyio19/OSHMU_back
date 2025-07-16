from modeltranslation.translator import register, TranslationOptions
from apps.SuperAdmin.models import Faculty, Speciality, Document, Institution, TitlesAdmin


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

@register(TitlesAdmin)
class TitlesAdminTranslationOptions(TranslationOptions):
    fields = ('full_name', 'faculty', 'institution', 'type_institution', 'address',
              'phone_number', 'students', 'institution_organization', 'course', 'metodist',
              'period', 'name', 'type', 'contacts', 'full_name_fkj', 'login', 'password')