from django.test import TestCase
# Create your tests here.
from django.contrib.auth.models import User
from ..models import Captain, Scheduler, TugBoat, ContainerBoat, Task, ScheduleEntry

class CaptainModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create(username='testuser', password='scy12345')
        cls.captain = Captain.objects.create(Account=cls.user, name="testuser", CaptainId="CAP123")

    def test_captain_str(self):
        self.assertEqual(str(self.captain), "CAP123")

    def test_captain_account_link(self):
        self.assertEqual(self.captain.Account, self.user)

class SchedulerModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create(username='testuser', password='scheduler123')
        cls.scheduler = Scheduler.objects.create(Account=cls.user, name="testuser", SchedulerId="SCH123")

    def test_scheduler_str(self):
        self.assertEqual(self.scheduler.SchedulerId, "SCH123")

    def test_scheduler_account_link(self):
        self.assertEqual(self.scheduler.Account, self.user)

class TugBoatModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        captain_user = User.objects.create(username='tugboatCaptain', password='tug123')
        cls.captain = Captain.objects.create(Account=captain_user, name="Tugboat Captain", CaptainId="TBC123")
        cls.tugboat = TugBoat.objects.create(TugBoatId="TB123", CaptainId=cls.captain)

    def test_tugboat_str(self):
        self.assertEqual(str(self.tugboat), "TB123")

    def test_tugboat_captain_link(self):
        self.assertEqual(self.tugboat.CaptainId, self.captain)

class ContainerBoatModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.containerBoat = ContainerBoat.objects.create(ContainerBoatID="CB123", Tonnage=5000, Country="Country X")

    def test_containerboat_str(self):
        self.assertEqual(str(self.containerBoat), "CB123")

from datetime import datetime
class TaskModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        container_boat = ContainerBoat.objects.create(ContainerBoatID="CBT123", Tonnage=10000, Country="Country Y")
        cls.task = Task.objects.create(ContainerBoatID=container_boat, RequiredTugBoat=2, startTime=datetime.now(), Action='INBOUND')
        cls.scheduleEntry = ScheduleEntry.objects.create(TaskId=cls.task)

    def test_task_defaults(self):
        self.assertEqual(self.task.State, 'Unscheduled')
        self.assertEqual(self.task.Action, 'INBOUND')
        
    def test_scheduleentry_defaults(self):
        self.assertEqual(self.scheduleEntry.Status, 'Scheduled')
