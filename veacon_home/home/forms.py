from django.forms import ModelForm

from .models import ContactModel


class FormContact(ModelForm):
    class Meta:
        model = ContactModel
        fields = ('name', 'phone', 'email', 'subject', 'message')