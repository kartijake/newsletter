from django.shortcuts import render
from .models import student_events,faculty_event,timeline,team

def student_details(request):
    
    std=student_events.objects.all()
    fac=faculty_event.objects.all()
    tim=timeline.objects.all()
    tm=team.objects.all()
    dic={'disc':std,'fac':fac,'tim':tim,'tm':tm}
    
   
    return render(request,'newsletter.html',dic)



# Create your views here.
