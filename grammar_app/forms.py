from django import forms
from grammar_app.models import DetailedEdit, QuickEdit

class DetailedEditForm(forms.ModelForm):
    class Meta:
        model = DetailedEdit
        exclude = ['time_created', 'time_updated']

        labels = {
            'content': '',
            'document_title': '',
            'error_list': '',
        }

    widgets = {
        'content': forms.Textarea(attrs={}),
        'document_title': forms.TextInput(attrs={}),
        'error_list': forms.Textarea(attrs={}),
    }


class QuickEditForm(forms.ModelForm):
    class Meta:
        model = QuickEdit
        exclude = ['time_created', 'time_updated']

        labels = {
            'input_text': '',
            'document_title': '',
            'corrected_text': '',
        }

    widgets = {
        'input_text': forms.Textarea(attrs={}),
        'document_title': forms.TextInput(attrs={}),
        'corrected_text': forms.Textarea(attrs={}),
    }