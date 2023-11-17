import TugBoat
import Task

class ScheduleEntry:
    def __init__(self) -> None:
        self.Tugboatlist=[]
        self.task=Task.Task()
        self.state="UNO"
        self.scheduleEntryID=""
    def getTugboatlist(self):
        return self.Tugboatlist
    def getTask(self):
        return self.task
    def getState(self):
        return self.state
    def getScheduleEntryID(self):
        return self.scheduleEntryID
    def addTugBoat(self,tugBoat):
        self.Tugboatlist.append(tugBoat)
    def setTask(self,task):
        self.task=task
    def setState(self,state):
        self.state=state
    def setScheduleEntryID(self,scheduleEntryID):
        self.scheduleEntryID=scheduleEntryID
    def removeTugBoat(self,tugBoat):
        self.Tugboatlist.remove(tugBoat)
    def __str__(self) -> str:
        return "Tugboatlist:"+str(self.Tugboatlist)+"\nTask:"+str(self.task)+"\nState:"+str(self.state)+"\nScheduleEntryID:"+str(self.scheduleEntryID)
    