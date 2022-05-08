from email.policy import default
from tkinter import CASCADE, Widget
from django.db import models
from ckeditor.fields import RichTextField
from datetime import datetime
from registrations.models import User
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField
from ckeditor.widgets import CKEditorWidget

# Create your models here.

class Page(models.Model):
    title = models.CharField(verbose_name='Título', max_length=350)
    content = RichTextField()
    creation_date = models.DateTimeField(blank=True, default=datetime.now)
    modification_date = models.DateTimeField(blank=True, default=datetime.now)
    image = models.ImageField(upload_to = 'profile_images', default='profile_images/default.png', blank = True )
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    
