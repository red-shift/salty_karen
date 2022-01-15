from django_registration.forms import RegistrationForm
from app_users.models import CustomUser
from django import forms


class CustomUserForm(RegistrationForm):
    birthdate = forms.DateField(widget=forms.SelectDateWidget())

    class Meta(RegistrationForm.Meta):
        model = CustomUser
