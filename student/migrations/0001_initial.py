# Generated by Django 2.2.7 on 2019-11-21 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='student_events',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discription', models.TextField()),
                ('image', models.ImageField(upload_to='media/students')),
            ],
        ),
    ]
