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
                task.RequiredTugBoat = requiredTugBoat
            if startTime is not None:
                task.startTime = startTime
            if endTime is not None:
                task.endTime = endTime
            if containerBoatId is not None:
                containerBoat = ContainerBoat.objects.get(ContainerBoatID=containerBoatId)
                task.ContainerBoatID = containerBoat
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
class SaveNewTaskView(View):
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
                containerBoat, created = ContainerBoat.objects.get_or_create(
                    ContainerBoatID = containerBoatId,
                    defaults={
                        'Tonnage': tonnage,
                        'Country': country,
                        'arrivalTime': arrivalTime,
                        'departureTime': leaveTime
                    }
                )
                Task.objects.create(
                    RequiredTugBoat=requiredTugBoat,
                    startTime=arrivalTime,
                    endTime=leaveTime,
                    ContainerBoatID=containerBoat,  
                    Action=action,
                    BerthId=0,
                    State='Unscheduled',
                )

            return JsonResponse({'success': True, 'status': 'success', 'message': 'Container Boat and Task saved successfully'})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

@method_decorator(csrf_exempt, name='dispatch')
class SaveEntryAndTaskView(View):
    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body)
            print("Received data:", data)
            entryId = data.get('entryId')
            plannedTime = data.get('plannedTime')
            containerBoatId = data.get('containerBoat')
            tugboat = data.get('tugboat')
            berth = data.get('berth')
            action = data.get('action')

            try:
                entry = ScheduleEntry.objects.get(ScheduleEntryId=entryId)
            except ScheduleEntry.DoesNotExist:
                 return JsonResponse({'error': f'Task with id={taskId} does not exist'}, status=404)
                  
            if plannedTime is not None:
                entry.startTime = plannedTime
            if containerBoat is not None:
                containerBoat = ContainerBoat.objects.get(ContainerBoatID=containerBoatId)
                entry.TaskId.ContainerBoatID = containerBoat
            if action is not None:
                entry.Action = action
            if berth is not None:
                entry.BerthId = berth
            if tugboat is not None:
                entry.listOfTugBoats = tugboat
            entry.save()
            return JsonResponse({'success': True, 'status': 'success', 'message': 'Schedule Entry Saved successfully'})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)    


from django.views.decorators.http import require_http_methods
from .ImportData import dataIntoDatabase_ContainerBoat, createTask
from django.core.files.storage import default_storage
import pandas as pd
import os
@csrf_exempt
@require_http_methods(["POST"])
def upload_task_data(request):
    if 'task_data' not in request.FILES:
        return JsonResponse({'error': 'No file uploaded.'}, status=400)
    
    task_data = request.FILES['task_data']

    temp_dir = os.path.join('system/temp')
    if not os.path.exists(temp_dir):
        os.makedirs(temp_dir)
    path = default_storage.save('system/temp/' + task_data.name, task_data)
    print(path)
    
    try:
        data = pd.read_excel(path, header=None)
        data=data.iloc[1:,:]
        df=pd.DataFrame(data)
        df.columns=['ContainerBoatID','Tonnage','Country','arrivalTime','departureTime']
        data = df
        dataIntoDatabase_ContainerBoat(data)
        createTask()
        default_storage.delete(path)
        
        return JsonResponse({'message': 'File processed successfully.'})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
    
def upload_tug_boat_data(request):
    pass

from .ExportData import DataTOExcel
@csrf_exempt
@require_http_methods(["POST"])
def publish_data(request):
    try:
        DataTOExcel()
        return JsonResponse({'message': 'Published successfully.'})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


from .serializers import (
    CaptainSerializer, 
    SchedulerSerializer, 
    TaskSerializer, 
    ContainerBoatSerializer, 
    BerthSerializer, 
    ScheduleEntrySerializer,
    TugBoatSerializer 
)
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
    queryset = Task.objects.all().order_by('startTime')
    serializer_class = TaskSerializer  

class BerthViewSet(viewsets.ModelViewSet):
    queryset = Berth.objects.all()
    serializer_class = BerthSerializer  

class ContainerBoatViewSet(viewsets.ModelViewSet):
    queryset = ContainerBoat.objects.all()
    serializer_class = ContainerBoatSerializer  

class ScheduleEntryViewSet(viewsets.ModelViewSet):
    queryset = ScheduleEntry.objects.all().order_by('TaskId__startTime')
    serializer_class = ScheduleEntrySerializer  

class TugBoatViewSet(viewsets.ModelViewSet):
    queryset = TugBoat.objects.all()
    serializer_class = TugBoatSerializer  