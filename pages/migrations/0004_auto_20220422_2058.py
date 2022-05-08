# Generated by Django 3.2.13 on 2022-04-22 23:58


from django.db import migrations, models
import ckeditor.fields

class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_auto_20220416_1230'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='image',
            field=models.ImageField(default='default.png', upload_to='profile_images'),
        ),
        migrations.AlterField(
            model_name='page',
            name='content',
            field= ckeditor.fields.RichTextField(),
        ),
    ]