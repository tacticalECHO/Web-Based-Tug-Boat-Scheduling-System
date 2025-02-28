"""created by Team 10, ©2024"""
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
                # Remove original relationship
                try:
                    tug = TugBoat.objects.get(CaptainId=captain)
                    tug.CaptainId = None
                    print("Captain: " + str(captain.CaptainId) + " is removed from Tug Boat: " + tug.TugBoatId)
                    tug.save()
                except TugBoat.DoesNotExist:
                    print(str(captain.CaptainId)+" has not tug boat")
                if captain.Account:
                    captain.Account.delete()
            return JsonResponse({'message': 'Captains deleted successfully'}, status=200)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

@method_decorator(csrf_exempt, name='dispatch')
class DeleteTasksView(View):
    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body)
            ids = data.get('ids', [])
            print(ids)
            tasks = Task.objects.filter(TaskId__in=ids)
           
            print(tasks)
            for task in tasks:
                task.delete()

            return JsonResponse({'message': 'Tasks deleted successfully'}, status=200)
        except Exception as e:

            print(f"Error deleting tasks: {str(e)}")

            return JsonResponse({'error': str(e)}, status=400)
        
@method_decorator(csrf_exempt, name='dispatch')
class DeleteTugBoatView(View):
    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body)
            ids = data.get('ids', [])
            print(ids)
            tugboats= TugBoat.objects.filter(TugBoatId__in=ids)
           
            print(tugboats)
            for tugboat in tugboats:
                tugboat.delete()

            return JsonResponse({'message': 'Tugboats deleted successfully', 'success': True}, status=200)
        except Exception as e:

            print(f"Error deleting tugboats: {str(e)}")

            return JsonResponse({'error': str(e)}, status=400)

@method_decorator(csrf_exempt, name='dispatch')
class DeleteScheduleEntriesView(View):
    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body)
            ids = data.get('ids', [])
            tasks = ScheduleEntry.objects.filter(TaskId__in=ids)
            print(tasks)

            for task in tasks:
                if task.TaskId:
                    task.TaskId.delete()

            return JsonResponse({'message': 'Schedules deleted successfully'}, status=200)
        except Exception as e:

            print(f"Error deleting tasks: {str(e)}")

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

@method_decorator(csrf_exempt, name='dispatch')
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
                user = User.objects.create_superuser(username=username, email='admin@gmail.com', password=password, first_name=name)
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

# @method_decorator(csrf_exempt, name='dispatch')
# class UpdateTaskView(View):
#     def post(self, request, *args, **kwargs):
#         try:
#             data = json.loads(request.body)
#             print("Received data:", data)
#             taskId = data.get('taskId')
#             requiredTugBoat = data.get('requiredTugBoat')
#             startTime = data.get('startTime')
#             endTime = data.get('endTime')
#             containerBoatId = data.get('containerBoatId')
#             action = data.get('action')
#             berthId = data.get('berthId')
#             state = data.get('state')
#             try:
#                 task = Task.objects.get(TaskId=taskId)
#             except Task.DoesNotExist:
#                  return JsonResponse({'error': f'Task with id={taskId} does not exist'}, status=404)
                  
#             if requiredTugBoat is not None:
#                 task.RequiredTugBoat = requiredTugBoat
#             if startTime is not None:
#                 task.startTime = startTime
#             if endTime is not None:
#                 task.endTime = endTime
#             if containerBoatId is not None:
#                 containerBoat = ContainerBoat.objects.get(ContainerBoatID=containerBoatId)
#                 task.ContainerBoatID = containerBoat
#             if action is not None:
#                 task.Action = action
#             if berthId is not None:
#                 task.BerthId = berthId
#             if state is not None:
#                 task.State = state
#             task.save()
#             return JsonResponse({'success': True, 'status': 'success', 'message': 'Task Updated successfully'})
#         except Exception as e:
#             return JsonResponse({'error': str(e)}, status=400)

from django.utils.dateparse import parse_datetime
from django.utils.timezone import make_aware, get_default_timezone, now
@method_decorator(csrf_exempt, name='dispatch')
class UpdateScheduleEntryView(View):
    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body)
            print("Received data:", data)
            entryId = data.get('entryId')
            newState = data.get('newState')
            timeStampStr = data.get('timeStamp')
            print(timeStampStr)
            if timeStampStr:
                timeStamp = parse_datetime(timeStampStr)
                if timeStamp and not timeStamp.tzinfo:
                    timeStamp = make_aware(timeStamp, get_default_timezone())
                timeStamp = timeStamp.astimezone(get_default_timezone())
                timeStamp = timeStamp.replace(second = 0,microsecond = 0, tzinfo=None)
            else:
                timeStamp = None
            print(timeStamp)

            entry = ScheduleEntry.objects.filter(ScheduleEntryId=entryId).first()
            if entry:
                entry.Status = newState
                print("1")
                if newState == 'Confirmed':
                    entry.StartTime = timeStamp
                    print(entry.StartTime)
                elif newState == 'Completed':
                    entry.EndTime = timeStamp
                entry.save()
                print("1")
                return JsonResponse({'success': True, 'message': 'Entry updated successfully.'})
            else:
                return JsonResponse({'error': 'ScheduleEntry not found'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

@method_decorator(csrf_exempt, name='dispatch')
class PublishView(View):
    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body)
            timeStampStr = data.get('timeStamp')
            print(timeStampStr)
            if timeStampStr:
                timeStamp = parse_datetime(timeStampStr)
                if timeStamp and not timeStamp.tzinfo:
                    timeStamp = make_aware(timeStamp, get_default_timezone())
                timeStamp = timeStamp.astimezone(get_default_timezone())
                timeStamp = timeStamp.replace(second = 0,microsecond = 0, tzinfo=None)
            else:
                timeStamp = None
            for entry in ScheduleEntry.objects.all():
                entry.PublishTime = timeStamp
                entry.save()
            return JsonResponse({'success': True, 'message': 'Entries published successfully.'})
        except Exception as e:
            print(e)
            return JsonResponse({'error': str(e), 'success': False})
        
@method_decorator(csrf_exempt, name='dispatch')
class SaveNewTaskView(View):
    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body)
            print("Received data:", data)
            containerBoatId = data.get('containerBoatId')
            tonnage = data.get('tonnage')
            country = data.get('country')
            time = data.get('time')
            berthId = data.get('berthId')
            # leaveTime = data.get('leaveTime')
            requiredTugBoat = data.get('requiredTugBoat')
            action = data.get('action')

            with transaction.atomic():
                # Create a new ContainerBoat or retrieve an existing one
                containerBoat, created = ContainerBoat.objects.get_or_create(
                    ContainerBoatID = containerBoatId,
                    defaults={
                        'Tonnage': tonnage,
                        'Country': country,
                        #'arrivalTime': arrivalTime,
                        #'departureTime': leaveTime
                    }
                )
                Task.objects.create(
                    # RequiredTugBoat=requiredTugBoat,
                    startTime=time,
                    ContainerBoatID=containerBoat,
                    RequiredTugBoat = requiredTugBoat, 
                    Action=action,
                    BerthId=int(berthId),
                    State='Unscheduled',
                )

            return JsonResponse({'success': True, 'status': 'success', 'message': 'Container Boat and Task saved successfully'})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
        
@method_decorator(csrf_exempt, name='dispatch')
class UpdateTugBoatView(View):
    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body)
            print("Received data:", data)

            tugboatId = data.get('tugboatId')
            captainId = data.get('captainId')
            startTime = data.get('startTime')
            endTime = data.get('endTime')
            status = data.get('status')
            message = ''

            if captainId is not None and captainId != '':
                captainId = str(captainId.split()[0])
                # Get the Captain object
                captain = Captain.objects.get(CaptainId=captainId)
                
                # Remove original relationship
                try:
                    tug = TugBoat.objects.get(CaptainId=captain)
                    tug.CaptainId = None
                    message = "Captain: " + str(captain.CaptainId) + " is removed from Tug Boat: " + tug.TugBoatId
                    tug.save()
                except TugBoat.DoesNotExist:
                    message = 'success'

            # Get or create TugBoat object
                with transaction.atomic():
                    tugboat, created = TugBoat.objects.get_or_create(
                        TugBoatId=tugboatId,
                        defaults={
                            'CaptainId': captain,
                            'StartWorkingTime': startTime,
                            'EndWorkingTime': endTime,
                        }
                    )
                if not created:
                    tugboat.CaptainId = captain

            # Update TugBoat attributes based on request data
            else:
                with transaction.atomic():
                    tugboat, created = TugBoat.objects.get_or_create(
                        TugBoatId=tugboatId,
                        defaults={
                            'CaptainId': None,
                            'StartWorkingTime': startTime,
                            'EndWorkingTime': endTime,
                        }
                    )
                if not created:
                    tugboat.CaptainId = None
                    if startTime is not None:
                        tugboat.StartWorkingTime = startTime
                    if endTime is not None:
                        tugboat.EndWorkingTime = endTime
                    if status is not None:
                        tugboat.CurrentStatus = status
            tugboat.save()

            return JsonResponse({'success': True, 'message': message})
        except Exception as e:
            print(e)
            return JsonResponse({'error': str(e)}, status=400)

from .Schedule import AutoSchedule, ifTugBoatAvailable, AutoSchedule_Reschedule

@method_decorator(csrf_exempt, name='dispatch')
class UpdateEntryAndTaskView(View):
    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body)
            print("Received data:", data)
            scheduleEntryId = data.get('entryId')
            taskId = data.get('taskId')
            startTime = data.get('plannedTime')
            containerBoatId = data.get('containerBoatId')
            removeTugBoatId = data.get('removeTugBoatId')
            newTugBoatId = data.get('newTugBoatId')
            berthId = data.get('berthId')
            action = data.get('action')
            #tugboat conflict value
            tugboatConflict = False
            tugConflictList = set()
            #time conflict value
            timeConflict = False
            totalTugboat = 0

            task = Task.objects.get(TaskId=taskId)
            try:
                if startTime is not None:
                    task.startTime = parse_datetime(startTime)
                    task.save()
                    if task.State == 'Scheduled' and scheduleEntryId is not None:
                        entry = ScheduleEntry.objects.get(ScheduleEntryId=scheduleEntryId)
                        tugBoatList = entry.listOfTugBoats.all()
                        list = set()
                        for tugboat in tugBoatList: # check for current tugboat availability
                            available, type = ifTugBoatAvailable(tugboat, task)
                            if not available:
                                timeConflict = True
                                totalTugboat+=1
                                list.add(tugboat.TugBoatId)
                                entry.listOfTugBoats.remove(tugboat)
                            entry.save()

                if containerBoatId is not None:
                    containerBoat = ContainerBoat.objects.get(ContainerBoatID=containerBoatId)
                    task.ContainerBoatID = containerBoat
                    task.save()
                if berthId is not None:
                    task.BerthId = berthId
                    task.save()
                if action is not None:
                    task.Action = str(action)
                    task.save()
                    print(str(action))
            except Exception as e:
                print(e)
                return JsonResponse({'error': e}, status=404) 

            if scheduleEntryId is not None:
                entry = ScheduleEntry.objects.filter(ScheduleEntryId=scheduleEntryId).first()

                if removeTugBoatId is not None:
                    try:
                        removeTugBoat = TugBoat.objects.get(TugBoatId=removeTugBoatId)
                        entry.listOfTugBoats.remove(removeTugBoat)
                        if entry.listOfTugBoats.count() <= 0:
                            entry.TaskId.State = 'Unscheduled'
                            entry.TaskId.TaskManual = 0
                            entry.TaskId.save()
                            entry.delete()
                            print('Entry deleted')
                    except TugBoat.DoesNotExist:
                        return JsonResponse({'error': f'Tugboat with id={removeTugBoatId} does not exist'}, status=404)  
                if newTugBoatId is not None:
                    try:
                        if newTugBoatId != "":
                            newTugBoat = TugBoat.objects.get(TugBoatId=newTugBoatId)
                            available, type = ifTugBoatAvailable(newTugBoat, task)
                            if not available:
                                if type != "Maintenance" and type != "NotWork":
                                    tugboatConflict = True
                                    tugConflictList.add(type)
                            else:
                                task.TaskManual = 1
                                task.save()
                                entry.listOfTugBoats.add(newTugBoat)
                                entry.save()
                                    
                    except TugBoat.DoesNotExist:
                        return JsonResponse({'error': f'Tugboat with id={newTugBoatId} does not exist'}, status=404)  
            
            if timeConflict: # request for
                conflictList = ", ".join(list)
                response = JsonResponse({'success': True,'timeConflict': timeConflict, 'tugboat': conflictList, 'total': totalTugboat})
            elif tugboatConflict:
                conflictedEntries  = ", ".join(tugConflictList)
                response = JsonResponse({'success': True, 'tugboat': newTugBoatId, 'tugboatConflict': tugboatConflict, 'conflictList':  conflictedEntries})
            else:
                response = JsonResponse({'success': True})
            return response
        except Exception as e:
            print(e)
            return JsonResponse({'error': str(e)}, status=400)

@method_decorator(csrf_exempt, name='dispatch')
class ManualScheduleView(View):
    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body)
            print("Received data:", data)
            taskId = data.get('taskId')
            tugBoatIds = data.get('tugBoatList')

            tugBoatList = TugBoat.objects.filter(TugBoatId__in=tugBoatIds)
            tugboatConflict = False
            tugboatMaintenance = False
            tugboatNotWork = False
            conflictEntry = set()
            conflictList = set()

            # create schedule entry for task
            task = Task.objects.filter(TaskId=taskId).first()
            scheduleEntry = ScheduleEntry.objects.create(
                TaskId = task,
                Status = "Scheduled",
                )
            scheduleEntry.listOfTugBoats.set(tugBoatList)
            task.State = "Scheduled"
            task.TaskManual = 1
            task.save()
            print("New Schedule Entry Created")

            # find for conflicted schedule entry
            # if scheduledList:
            #     for scheduled in scheduledList:
            for tugboat in tugBoatList:
                availability, type = ifTugBoatAvailable(tugboat, task)
                if not availability:
                    if type != "Maintenance" and type != "NotWork":
                        tugboatConflict = True
                        conflictList.add(str(tugboat.TugBoatId))
                        conflictEntry.add(type)
            
            if not tugboatMaintenance and not tugboatNotWork and not tugboatConflict:
                response = JsonResponse({'success': True})
            if tugboatMaintenance or tugboatNotWork or tugboatConflict:
                AutoSchedule_Reschedule()
                print('rescheduled complete')
                conflict = ''
                for boat in conflictList:
                    for entry in conflictEntry:
                        conflict = conflict + boat + ' : ' + entry + '\n'
                # print("conflicted entries " + conflictedEntries + " rescheduling")
                response = JsonResponse({'success': True, 'conflict': tugboatConflict, 'conflictList':  conflict})
            return response
        except Exception as e:
            print(e)
            return JsonResponse({'error': str(e)}, status=400)
        
@method_decorator(csrf_exempt, name='dispatch')
class TugBoatRescheduleView(View):
    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body)
            print("Received data:", data)
            total = data.get('total')
            entryId = data.get('entryId')
            taskId = data.get('taskId')
            
            entry = ScheduleEntry.objects.get(ScheduleEntryId=entryId)
            task = Task.objects.get(TaskId=taskId)
            all_tugboats = TugBoat.objects.all()

            index = total
            added = 0
            insufficient = False
            while index>0:
                for tugboat in all_tugboats:
                    available, type = ifTugBoatAvailable(tugboat, task)
                    if available:
                        entry.listOfTugBoats.add(tugboat)
                        entry.save()
                        added+=1
                        break
                index-=1
            if added < total:
                insufficient = True
            return JsonResponse({'success': True, 'insufficient': insufficient})
        except Exception as e:
            print(e)
            return JsonResponse({'error': str(e)}, status=400)         
        
@method_decorator(csrf_exempt, name='dispatch')
class AutoScheduleView(View):
    def post(self, request, *args, **kwargs):
        success, message = AutoSchedule()

        if success:
            return JsonResponse({'success': True, 'message': message})
        else:
            return JsonResponse({'success': False, 'message': message})
        
@method_decorator(csrf_exempt, name='dispatch')
class AutoRescheduleView(View):
    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body)
            print("Received data:", data)
            tugboatId = data.get('tugboatId')
            entryId = data.get('entryId')
            print('auto-reschedule')
            if entryId is not None:
                print('entryId available')
                if tugboatId is not None:
                    print('tugboatId available')
                    entry = ScheduleEntry.objects.get(ScheduleEntryId=entryId)
                    task = Task.objects.get(TaskId=entry.TaskId.TaskId)
                    task.TaskManual = 1
                    task.save()
                    tugboat = TugBoat.objects.get(TugBoatId=tugboatId)
                    entry.listOfTugBoats.add(tugboat)
                    entry.save()
                    print('entry saved')
            success, message = AutoSchedule_Reschedule()
            print(success)
            return JsonResponse({'success': success})
        except Exception as e:
            print(e)
            return JsonResponse({'success': False})

from django.views.decorators.http import require_http_methods
from .ImportData import dataIntoDatabase_ContainerBoat, createTask, dataIntoDatabase_TugBoat
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
        df.columns=['ContainerBoatID','Tonnage','Country','ScheduleTime','Action','BerthID']
        data = df
        dataIntoDatabase_ContainerBoat(data)
        createTask(data)
        default_storage.delete(path)
        
        return JsonResponse({'message': 'File processed successfully.'})
    except Exception as e:
        default_storage.delete(path)
        print (e)
        return JsonResponse({'error': str(e)}, status=500)

@csrf_exempt
@require_http_methods(["POST"])
def upload_tug_boat_data(request):
    if 'tugboat_data' not in request.FILES:
        return JsonResponse({'error': 'No file uploaded.'}, status=400)
    
    tugboat_data = request.FILES['tugboat_data']

    temp_dir = os.path.join('system/temp')
    if not os.path.exists(temp_dir):
        os.makedirs(temp_dir)
    path = default_storage.save('system/temp/' +tugboat_data.name, tugboat_data)
    print(path)
    
    try:
        data = pd.read_excel(path)
        print("1")
        dataIntoDatabase_TugBoat(data)
        default_storage.delete(path)
        
        return JsonResponse({'message': 'File processed successfully.'})
    except Exception as e:
        default_storage.delete(path)
        print(e)
        return JsonResponse({'error': str(e)}, status=500)

from .ExportData import DataTOExcel
@csrf_exempt
@require_http_methods(["POST"])
def publish_data(request):
    try:
        DataTOExcel()
        return JsonResponse({'message': 'Published successfully.'})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

from .ExportData import DataToExcel_captain
@csrf_exempt
@require_http_methods(["POST"])
def download_captain(request):
    try:
        data = json.loads(request.body)
        print("Received data:", data)
        captain_id = data.get('captainId')
        if captain_id:
            DataToExcel_captain(captain_id)
            return JsonResponse({'message': 'Published successfully.'})
        else:
            return JsonResponse({'error': str(e)}, status=404)
    except Exception as e:
        print(e)
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
from datetime import datetime
class CaptainViewSet(viewsets.ModelViewSet):
    queryset = Captain.objects.all().order_by('CaptainId')
    serializer_class = CaptainSerializer
    def list(self, request, *args, **kwargs):
        self.update_tugboatStatus()
        return super(CaptainViewSet, self).list(request, *args, **kwargs)
#    def update_tugboatStatus(self):
#        current_time = datetime.now().time()
#        TugBoatList=TugBoat.objects.all()
#        for boat in TugBoatList:
#            if boat.StartWorkingTime<=current_time and boat.EndWorkingTime>=current_time:
#                #for tugboat in schedule.listOfTugBoats.all():
#                boat.CurrentStatus='Busy'
#                boat.save()
#            elif boat.EndWorkingTime<current_time:
#                #for tugboat in schedule.listOfTugBoats.all():
#                    boat.CurrentStatus='Free'
#                    boat.save()
    def update_tugboatStatus(self):
        ScheduleEntryList=ScheduleEntry.objects.all()
        if ScheduleEntryList!=None:
            for schedule in ScheduleEntryList:
                if schedule.StartTime!=None and schedule.StartTime.time()<=datetime.now().time() and schedule.EndTime==None:
                    for tugboat in schedule.listOfTugBoats.all():
                        for tugboat in schedule.listOfTugBoats.all():
                            tugboat.CurrentStatus='Busy'
                            tugboat.save()
                elif schedule.EndTime!=None and schedule.EndTime.time()<datetime.now().time():
                    for tugboat in schedule.listOfTugBoats.all():
                        for tugboat in schedule.listOfTugBoats.all():
                            tugboat.CurrentStatus='Free'
                            tugboat.save()
        else:
            TugBoatList=TugBoat.objects.all()
            for boat in TugBoatList:
                if boat.CurrentStatus=='Busy':
                    boat.CurrentStatus='Free'
                    boat.save()              
                

    # def update_tugboatStatus(self):
    #     ScheduleEntryList=ScheduleEntry.objects.all()
    #     for schedule in ScheduleEntryList:
    #         if schedule.StartTime<=datetime.datetime.now() and schedule.EndTime>=datetime.datetime.now():
    #             for tugboat in schedule.listOfTugBoats.all():
    #                 tugboat.CurrentStatus='Busy'
    #                 tugboat.save()
    #         elif schedule.EndTime<datetime.datetime.now():
    #             for tugboat in schedule.listOfTugBoats.all():
    #                 tugboat.CurrentStatus='Free'
    #                 tugboat.save()

class SchedulerViewSet(viewsets.ModelViewSet):
    queryset = Scheduler.objects.all()
    serializer_class = SchedulerSerializer

    def build_new_user(request):
        new_user = User.objects.create_user()

class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer

    def get_queryset(self):
        sort = self.request.query_params.get('sort')
        today_date = now().date()

        queryset = Task.objects.filter(
                startTime__date=today_date
            ).order_by('TaskId')
        
        if sort == 'true':
            queryset = Task.objects.filter(
                startTime__date=today_date
            ).order_by('startTime')

        return queryset
    
class BerthViewSet(viewsets.ModelViewSet):
    queryset = Berth.objects.all().order_by('BerthId')
    serializer_class = BerthSerializer  

class ContainerBoatViewSet(viewsets.ModelViewSet):
    queryset = ContainerBoat.objects.all().order_by('ContainerBoatID')
    serializer_class = ContainerBoatSerializer  

class ScheduleEntryViewSet(viewsets.ModelViewSet):
    serializer_class = ScheduleEntrySerializer

    def get_queryset(self):
        sort = self.request.query_params.get('sort')
        today_date = now().date()

        queryset = ScheduleEntry.objects.filter(
                TaskId__startTime__date=today_date
            ).order_by('ScheduleEntryId')
        
        if sort == 'true':
            queryset = ScheduleEntry.objects.filter(
                TaskId__startTime__date=today_date
            ).order_by('TaskId__startTime')
            
        return queryset

class TugBoatViewSet(viewsets.ModelViewSet):
    serializer_class = TugBoatSerializer  

    def get_queryset(self):
        queryset = TugBoat.objects.all().order_by('TugBoatId')
        
        # Check if you want to filter the queryset
        taskId = self.request.query_params.get('taskId')
        
        if taskId is not None:
            task = Task.objects.get(TaskId=taskId)
            filtered_tugboats = set()
            for tugboat in queryset:
                    filtered_tugboats.add(tugboat)
                    # print(tugboat)
                    status, type = ifTugBoatAvailable(tugboat, task)
                    if not status:
                        if type == 'Maintenance' or type == 'NotWork':
                            filtered_tugboats.discard(tugboat)

            all_entries = ScheduleEntry.objects.all()
            for entry in all_entries:
                if entry.TaskId.TaskManual == 1 and entry.Status != 'Completed':
                    tugboatList = entry.listOfTugBoats.all()
                    for tugboat in tugboatList:
                        status, type = ifTugBoatAvailable(tugboat, task)
                        if not status:
                            filtered_tugboats.discard(tugboat)
            # print(str(filtered_tugboats))
            queryset = sorted(filtered_tugboats, key=lambda x: x.TugBoatId)
        
        return queryset