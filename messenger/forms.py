from datetime import datetime
from django import forms
from ckeditor.fields import RichTextField
from django.db import models
from .models import Message

class MessageForm(forms.Form):
    class Meta:
        model = Message
        fields = ['title', 'content', 'receiver']
        widgets = {
            'content': forms.Textarea(attrs={'class':'form-control mt-3', 'rows':3, 'placeholder':'Mensaje'}),
            'title': forms.TextInput(attrs={'class':'form-control mt-3', 'placeholder':'Título'}),
        }
  
  