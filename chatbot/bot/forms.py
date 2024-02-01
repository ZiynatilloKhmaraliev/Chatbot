from django import forms
from .models import Message
from django.contrib.auth.models import User

class MessageForm(forms.ModelForm):
    class Meta:
        model=Message
        fields=('text',)
        exclude=['user','created','answer']
    text=forms.CharField(widget=forms.TextInput(attrs={
       'class':"form-control message-input",
       'placeholder':"Type your message..."
    }))

