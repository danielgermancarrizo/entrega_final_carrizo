from email.policy import default
from tokenize import blank_re
from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.

class Profile(models.Model):
    full_name = models.CharField(verbose_name='name', max_length=100)
    description = RichTextField()
    url_web = models.URLField(blank=True, null = True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to = 'profile_images', default='default.png', null = True, blank = True )
    
    def __str__(self) -> str:
        return self.user.username   