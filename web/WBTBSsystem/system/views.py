from django.shortcuts import render
from django.http import HttpResponse
from .models import Members, Captain, TugBoat, ContainerBoat, Task, ScheduleEntry, User
from django.template import loader
# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the system index.")
def detail(request):
    memberlist=Members.objects.all()
    context={'memberlist':memberlist}
    return render(request, 'index.html', context)
def team(request):
    return render(request, 'index.html')
def TugBoatDetail(request):
    tugboatList=TugBoat.objects.all()
    context={'tugboatList':tugboatList}
    return render(request, 'TugBoatDetail.html', context)
def ScheduleDetail(request):
    scheduleList=ScheduleEntry.objects.all()
    context={'scheduleList':scheduleList}
    return render(request, 'ScheduleDetail.html', context)
def CaptainDetail(request):
    captainList=Captain.objects.all()
    context={'captainList':captainList}
    return render(request, 'CaptainDetail.html', context)