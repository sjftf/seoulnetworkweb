# Generated by Django 3.2.7 on 2021-10-18 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('story', '0003_auto_20210922_1150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='publish',
            field=models.DateField(blank=True, verbose_name='date published'),
        ),
    ]