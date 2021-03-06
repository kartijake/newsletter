# Generated by Django 2.2.7 on 2019-11-23 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_auto_20191123_2005'),
    ]

    operations = [
        migrations.CreateModel(
            name='faculty_event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_s', models.ImageField(upload_to='faculty')),
                ('caption_s', models.CharField(max_length=20)),
                ('description_s', models.TextField()),
                ('date_s', models.TextField(blank=True)),
                ('place', models.TextField(blank=True, default='DBIT')),
            ],
        ),
    ]
