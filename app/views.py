from django.shortcuts import render
from app.models import*

# Create your views here.

def display_topics(request):
    topics=Topic.objects.all()
    d={'topics':topics}
    return render(request,'display_topics.html',d)

def display_webpages(request):
    webpages=Webpage.objects.all()
    d={'webpages':webpages}
    return render(request,'display_webpages.html',d)


def display_accessrecord(request):
    accessrecord=AccessRecords.objects.all()
    d={'accessrecord':accessrecord}
    return render(request,'display_accessrecord.html',d)
    