# Generated by Django 3.2.13 on 2022-05-06 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0011_page_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='image',
            field=models.ImageField(blank=True, default='profile_images/default.png', upload_to='profile_images'),
        ),
    ]
