# Generated by Django 2.2.7 on 2019-11-23 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student_events',
            name='discription',
        ),
        migrations.AddField(
            model_name='student_events',
            name='caption',
            field=models.CharField(default='dsd', max_length=20),
        ),
        migrations.AddField(
            model_name='student_events',
            name='description',
            field=models.TextField(default='no dec'),
        ),
        migrations.AlterField(
            model_name='student_events',
            name='image',
            field=models.ImageField(upload_to='students'),
        ),
    ]
