# Generated by Django 3.2.13 on 2022-04-21 15:31

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100, verbose_name='Título')),
                ('description', ckeditor.fields.RichTextField()),
                ('url_web', models.URLField(blank=True, null=True)),
                ('email', models.DateTimeField(blank=True, null=True)),
                ('password', models.DateTimeField(blank=True, null=True)),
                ('avatar', models.ImageField(default='default.png', upload_to='images')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
