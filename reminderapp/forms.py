from django import forms
from .models import Message

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['name', 'email', 'phone', 'time', 'date', 'message']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }
