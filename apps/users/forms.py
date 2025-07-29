# forms.py
from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from .models import User

class UserAdminCreationForm(forms.ModelForm):
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('full_name', 'password', 'role', 'course', 'faculty', 'institution', 'speciality')

    def clean_password(self):
        return self.cleaned_data['password']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user
