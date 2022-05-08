from datetime import datetime
from django import forms
from ckeditor.fields import RichTextField
from django.db import models
from pages.models import Page
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.widgets import CKEditorWidget

class PageForm(forms.Form):
    class Meta:
        model = Page
        fields = ['title', 'content', 'image']
        widgets = {
            'image': forms.ClearableFileInput(attrs={'class':'form-control-file mt-3'}),
            'content' : forms.CharField(widget = CKEditorWidget()),
            'title': forms.TextInput(attrs={'class':'form-control mt-3', 'placeholder':'Título'}),
        }
  
  