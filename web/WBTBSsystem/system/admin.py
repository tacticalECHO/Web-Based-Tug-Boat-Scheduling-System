from django.contrib import admin


# Register your models here.
from .models import Members, Captain, TugBoat, ContainerBoat, Task, ScheduleEntry, UUser

admin.site.register(Members)
admin.site.register(Captain)
admin.site.register(TugBoat)
admin.site.register(ContainerBoat)
admin.site.register(Task)
admin.site.register(ScheduleEntry)
admin.site.register(UUser)



