from rest_framework import serializers
from apps.SuperAdmin.models import Institution, Faculty, Speciality, Document



class FacultySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Faculty
        fields = ['id', 'faculty']


class SpecialitySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Speciality
        fields = ['id', 'speciality']

        
class InstitutionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Institution
        fields = ["id", "logo", "name", "type", "contact", "address"]
        read_only_fields = ['id']
        


class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = [
            'id', 'title', 'content'
        ]
        read_only_fields = ['id']