# Generated by Django 3.2.7 on 2021-10-18 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('story', '0004_alter_story_publish'),
    ]

    operations = [
        migrations.AddField(
            model_name='story',
            name='writer',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
