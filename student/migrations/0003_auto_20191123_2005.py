# Generated by Django 2.2.7 on 2019-11-23 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_auto_20191123_1933'),
    ]

    operations = [
        migrations.AddField(
            model_name='student_events',
            name='date',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='student_events',
            name='place',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
