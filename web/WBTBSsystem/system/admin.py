from django.contrib import admin


# Register your models here.
from .models import Scheduler, Captain, TugBoat, ContainerBoat, Task, ScheduleEntry

admin.site.register(Captain)
admin.site.register(TugBoat)
admin.site.register(ContainerBoat)
admin.site.register(Task)
admin.site.register(ScheduleEntry)
admin.site.register(Scheduler)



