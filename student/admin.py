from django.contrib import admin
from .models import student_events,faculty_event,timeline,team

admin.site.register(student_events)
admin.site.register(faculty_event)
admin.site.register(timeline)
admin.site.register(team)
# Register your models here.
