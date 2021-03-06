# Generated by Django 2.2.7 on 2019-11-23 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0004_faculty_event'),
    ]

    operations = [
        migrations.CreateModel(
            name='timeline',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='timeline')),
                ('description', models.TextField()),
                ('caption', models.CharField(max_length=20)),
                ('date', models.CharField(max_length=20)),
            ],
        ),
    ]
