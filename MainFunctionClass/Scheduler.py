from viewable import viewable
from ScheduleEntry import ScheduleEntry
from Captain import Captain
from TugBoat import TugBoat
class Scheduler(viewable):
    def __init__(self):
        self.schedulerId = 0
        self.schedulelist = []
        self.CT_list = []
    def importTaskData():
        pass
    def deleteScheduleEntry(self, scheduleEntry):
        self.schedulelist.remove(scheduleEntry)
    def addScheduleEntry(self, scheduleEntry):
        self.schedulelist.append(scheduleEntry)
    def getScheduleEntry(self, scheduleEntryID):
        for scheduleEntry in self.schedulelist:
            if scheduleEntry.getScheduleEntryID() == scheduleEntryID:
                return scheduleEntry
        return None
    def getSchedulelist(self):
        return self.schedulelist
    def getSchedulerId(self):
        return self.schedulerId
    def getCT_list(self):
        return self.CT_list
    def autoSchedule(self):
        pass
    def editScheduleEntry(self, scheduleEntry):
        pass
    def exportSchedule(self):
        pass
    def modify_CT_Captain(self, captain):
        pass
    def modify_CT_TugBoat(self, tugBoat):
        pass
    def add_CT(self, tugBoat, captain):
        self.CT_list.append([tugBoat, captain])
    def remove_CT(self, tugBoat, captain):
        self.CT_list.remove([tugBoat, captain])
    def setSchedulerId(self, schedulerId):
        self.schedulerId = schedulerId
    def search_in_CT_list(self,target):
        for i in self.CT_list:
            if i[0]==target or i[1]==target:
                return self.CT_list.index(i)
        return None
    def search_in_schedulelist(self,target):
        for i in self.schedulelist:
            if i==target:
                return self.schedulelist.index(i)
        return None
    def __str__(self) -> str:
        return "schedulerId:"+str(self.schedulerId)+"\nschedulelist:"+str(self.schedulelist)+"\nCT_list:"+str(self.CT_list)
