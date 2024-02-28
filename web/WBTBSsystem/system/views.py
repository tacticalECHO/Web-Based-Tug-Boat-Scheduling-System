from django.shortcuts import render
from django.http import HttpResponse
from .models import Captain, TugBoat, ContainerBoat, Task, ScheduleEntry, Scheduler, Berth
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
from django.db import transaction

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
            try:
                user.scheduler 
                is_scheduler = True
            except Scheduler.DoesNotExist:
                is_scheduler = False
            return JsonResponse({'success': True,
                                'is_staff': user.is_staff,
                                'is_captain': is_captain,
                                'is_scheduler': is_scheduler})
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

@method_decorator(csrf_exempt, name='dispatch')
class DeleteCaptainsView(View):
    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body)
            ids = data.get('ids', [])
            captains = Captain.objects.filter(CaptainId__in=ids)
            for captain in captains:
                if captain.Account:
                    captain.Account.delete()
            return JsonResponse({'message': 'Captains deleted successfully'}, status=200)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

@method_decorator(csrf_exempt, name='dispatch')
class DeleteSchedulersView(View):
    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body)
            ids = data.get('ids', [])
            schedulers = Scheduler.objects.filter(SchedulerId__in=ids)
            print(schedulers)
            for scheduler in schedulers:
                if scheduler.Account:
                    scheduler.Account.delete()            
            return JsonResponse({'message': 'Schedulers deleted successfully'}, status=200)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

class CreateUserView(View):
    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body)
            print("Received data:", data)
            username = data.get('username')
            name = data.get('name')
            position = data.get('position')
            password = data.get('password', '12345678')

            if position == 'Administrator':
                user = User.objects.create_superuser(username=username, email='example@gmail.com', password=password, first_name=name)
            else:
            
                user = User.objects.create_user(username=username, password=password, first_name=name)
                if position == 'Captain':
                    Captain.objects.create(Account=user, name=name, CaptainId=username)
                elif position == 'Scheduler':
                    Scheduler.objects.create(Account=user, name=name, SchedulerId=username)

            return JsonResponse({'status': 'success', 'message': 'User created successfully'})
        except Exception as e:
            print("Error:", e)
            return JsonResponse({'status': 'error', 'message': 'Invalid request'}, status=400)

@method_decorator(csrf_exempt, name='dispatch')
class SaveTaskView(View):
    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body)
            print("Received data:", data)
            taskId = data.get('taskId')
            requiredTugBoat = data.get('requiredTugBoat')
            startTime = data.get('startTime')
            endTime = data.get('endTime')
            containerBoatId = data.get('containerBoatId')
            action = data.get('action')
            berthId = data.get('berthId')
            state = data.get('state')

            try:
                task = Task.objects.get(TaskId=taskId)
            except Task.DoesNotExist:
                 return JsonResponse({'error': f'Task with id={taskId} does not exist'}, status=404)
                  
            if requiredTugBoat is not None:
                task.ReqauriedTugBoat = requiredTugBoat
            if startTime is not None:
                task.startTime = startTime
            if endTime is not None:
                task.endTime = endTime
            if containerBoatId is not None:
                task.ContainerBoatID = containerBoatId
            if action is not None:
                task.Action = action
            if berthId is not None:
                task.BerthId = berthId
            if state is not None:
                task.State = state
            task.save()
            return JsonResponse({'success': True, 'status': 'success', 'message': 'Task Saved successfully'})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

@method_decorator(csrf_exempt, name='dispatch')
class SaveContainerBoatView(View):
    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body)
            print("Received data:", data)
            containerBoatId = data.get('containerBoatId')
            tonnage = data.get('tonnage')
            country = data.get('country')
            arrivalTime = data.get('arrivalTime')
            leaveTime = data.get('leaveTime')
            requiredTugBoat = data.get('requiredTugBoat')
            action = data.get('action')

            with transaction.atomic():
                # Create a new ContainerBoat or retrieve an existing one
                # containerBoat, created = ContainerBoat.objects.get_or_create(
                #     ContainerBoatID = containerBoatId,
                #     defaults={
                #         'Tonnage': tonnage,
                #         'Country': country,
                #         'arrivalTime': arrivalTime,
                #         'departureTime': leaveTime
                #     }
                # )
                try:
                    containerBoat = ContainerBoat.objects.get(ContainerBoatID = containerBoatId)
                except ContainerBoat.DoesNotExist:
                    containerBoat = ContainerBoat(ContainerBoatID = containerBoatId, Tonnage = tonnage, Country = country, arrivalTime = arrivalTime, departureTime = leaveTime)
                    
                Task.objects.create(
                    ReqauriedTugBoat=requiredTugBoat,
                    startTime=arrivalTime,
                    endTime=leaveTime,
                    ContainerBoatID=containerBoat,  
                    Action=action,
                    BerthId='',
                    State='unscheduled',
                )

            return JsonResponse({'success': True, 'status': 'success', 'message': 'Container Boat and Task saved successfully'})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

from .serializers import CaptainSerializer, SchedulerSerializer, TaskSerializer, ContainerBoatSerializer, BerthSerializer
from rest_framework import viewsets

class CaptainViewSet(viewsets.ModelViewSet):
    queryset = Captain.objects.all()
    serializer_class = CaptainSerializer

class SchedulerViewSet(viewsets.ModelViewSet):
    queryset = Scheduler.objects.all()
    serializer_class = SchedulerSerializer

    def build_new_user(request):
        new_user = User.objects.create_user()

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer  

class BerthViewSet(viewsets.ModelViewSet):
    queryset = Berth.objects.all()
    serializer_class = BerthSerializer  

class ContainerBoatViewSet(viewsets.ModelViewSet):
    queryset = ContainerBoat.objects.all()
    serializer_class = ContainerBoatSerializer  