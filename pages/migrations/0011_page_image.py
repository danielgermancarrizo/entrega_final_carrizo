# Generated by Django 3.2.13 on 2022-04-24 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0010_remove_page_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='profile_images'),
        ),
    ]
