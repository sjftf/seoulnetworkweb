# Generated by Django 3.2.7 on 2021-09-21 13:54

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('story', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='story',
            options={'ordering': ('-publish',)},
        ),
        migrations.AddField(
            model_name='story',
            name='thumbnail',
            field=models.ImageField(blank=True, default='default.png', upload_to=''),
        ),
        migrations.AlterField(
            model_name='story',
            name='body',
            field=tinymce.models.HTMLField(),
        ),
    ]
