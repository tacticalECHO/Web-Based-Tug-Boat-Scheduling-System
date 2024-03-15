from django.test import TestCase, Client
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from ..models import Captain, Scheduler, TugBoat, ContainerBoat, Task, ScheduleEntry
from django.contrib.auth.models import User
from datetime import datetime
import requests

class TestAPIViews(StaticLiveServerTestCase):
    @classmethod
    def setUp(self):
        super().setUpClass()
        self.user = User.objects.create(username='testuser1')
        self.user.set_password('captain12345')
        self.user.save()
        self.captain = Captain.objects.create(Account=self.user, name="testuser1", CaptainId="CP0001")
        self.tugboat = TugBoat.objects.create(TugBoatId="TB123", CaptainId=self.captain)

        self.user = User.objects.create(username='testuser2', password='scheduler123')
        self.user.set_password('scheduler123')
        self.user.save()
        self.scheduler = Scheduler.objects.create(Account=self.user, name="testuser2", SchedulerId="SC0001")

        self.containerBoat = ContainerBoat.objects.create(ContainerBoatID="CB123", Tonnage=5000, Country="Country X")
        self.task = Task.objects.create(ContainerBoatID=self.containerBoat, RequiredTugBoat=2, startTime=datetime.now(), Action='INBOUND')
        self.scheduleEntry = ScheduleEntry.objects.create(TaskId=self.task)
    
    def test_login_view(self):
        self.client = Client()
        login_data = {'username': 'testuser1', 'password': 'captain12345'}
        response = self.client.post('/api/login/', data=login_data, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.json()['success'])
        login_data = {'username': 'testuser1', 'password': 'error'}
        response = self.client.post('/api/login/', data=login_data, content_type='application/json')
        self.assertEqual(response.status_code, 401)
        self.assertFalse(response.json()['success'])

    def test_change_password_view(self):
        self.client = Client()
        self.client.login(username='testuser1', password='captain12345')
        change_password_data = {'username': 'testuser1', 'password': 'newpassword123'}
        response = self.client.post('/api/change-password/', data=change_password_data, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.json()['success'])

        login_data = {'username': 'testuser1', 'password': 'newpassword123'}
        response = self.client.post('/api/login/', data=login_data, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.json()['success'])

    def test_create_user_view(self):
        self.client = Client()
        user_data = {
            'username': 'newuser',
            'name': 'New',
            'position': 'Captain',
        }
        response = self.client.post('/api/create-user/', data=user_data, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn('User created successfully', response.json()['message'])

    def test_delete_captains_view(self):
        self.client = Client()
        delete_captain_data = {'ids': [self.captain.CaptainId]}
        response = self.client.post('/api/captains-delete/', data=delete_captain_data, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Captains deleted successfully', response.json()['message'])

    def test_save_new_task(self):
        new_task_data = {
            'containerBoatId': 'CB456',
            'tonnage': 6000,
            'country': 'Country Y',
            'time': '2023-04-01T12:00:00',
            'berthId': 1,
            'action': 'INBOUND',
        }
        response = self.client.post('/api/save-newtask/', data=new_task_data, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Container Boat and Task saved successfully', response.json()['message'])

    def test_delete_tasks_view(self):
        self.client = Client()
        delete_task_data = {'ids': [2]}
        response = self.client.post('/api/tasks-delete/', data=delete_task_data, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Tasks deleted successfully', response.json()['message'])

    def test_delete_entry_view(self):
        self.client = Client()
        delete_task_data = {'ids': [2]}
        response = self.client.post('/api/scheduleentries-delete/', data=delete_task_data, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Schedules deleted successfully', response.json()['message'])

    def test_update_entry_view(self):
        self.client = Client()
        update_data = {'entryId': str(self.scheduleEntry.ScheduleEntryId),
                        'newState': 'Confirmed',
                        'timeStamp': '2024-03-15T15:00:00+0000',
                    }
        response = self.client.post('/api/update-schedule-entry', data=update_data, content_type='application/json')
        print(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertIn('Entry updated successfully.', response.json()['message'])

    def test_publish(self):
        publish_data = {'timeStamp': '2024-03-15T15:00:00+0000'}
        response = self.client.post('/api/update-publish-time', data=publish_data, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Entries published successfully.', response.json()['message'])


