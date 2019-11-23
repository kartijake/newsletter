from django.db import models

class student_events(models.Model):
    description =models.TextField(default="no dec")
    image=models.ImageField(upload_to='students')
    caption=models.CharField(max_length=20,default="dsd")
    date=models.CharField(max_length=20,blank=True)
    place=models.CharField(max_length=20,blank=True)


class faculty_event(models.Model):
    image_s=models.ImageField(upload_to='faculty')
    caption_s=models.CharField(max_length=20)
    description_s=models.TextField()
    date_s=models.TextField(blank=True)
    place=models.TextField(default='DBIT',blank=True)

class timeline(models.Model):
    image=models.ImageField(upload_to='timeline')
    description=models.TextField()
    caption=models.CharField(max_length=20)
    date=models.CharField(max_length=20)

class team(models.Model):
    image=models.ImageField(upload_to='team')
    name=models.CharField(max_length=30)
    designation=models.CharField(max_length=30)


# Create your models here.
