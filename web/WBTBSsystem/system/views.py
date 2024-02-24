from django.shortcuts import render
from django.http import HttpResponse
from .models import Members, Captain, TugBoat, ContainerBoat, Task, ScheduleEntry
from django.template import loader
# Create your views here.
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
import json
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User

@method_decorator(csrf_exempt, name='dispatch')
class LoginView(View):
    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            try:
                user.captain 
                is_captain = True
            except Captain.DoesNotExist:
                is_captain = False
            return JsonResponse({'success': True,
                                'is_captain': is_captain,})
        else:
            return JsonResponse({'success': False}, status=401)

@method_decorator(csrf_exempt, name='dispatch')
class ChangePasswordView(View):
    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        username = data.get('username')
        new_password = data.get('password')
        
        try:
            user = User.objects.get(username=username)
            user.set_password(new_password)
            user.save()
            return JsonResponse({'success': True})
        except User.DoesNotExist:
            return JsonResponse({'success': False}, status=401)
        
from .serializers import CaptainSerializer
from rest_framework import viewsets

class CaptainViewSet(viewsets.ModelViewSet):
    queryset = Captain.objects.all()
    serializer_class = CaptainSerializer
        

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