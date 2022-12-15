from django import forms
from .models import Email

class EmailForm(forms.ModelForm):
    class Meta:
        model = Email
        fields = ['subject','body']
        
        labels = {
            'subject' : 'Subject*',
            'body' : 'Email Body*',
        }
        widgets = {
            'subject' : forms.TextInput(attrs={
                'class' : 'form-control',
                'rows' : 1,
                'cols' : 100,
                'type' : 'text'
            }),
        }
        