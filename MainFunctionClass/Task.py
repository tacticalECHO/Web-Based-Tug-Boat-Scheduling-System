import ContainerBoat

class Task:
    def __init__(self) -> None:
        self.requiredTugBoat=0
        self.target=ContainerBoat.ContainerBoat()
        self.startTime=""
        self.endTime=""
        self.action="UNO"
        self.BerthId=0
    def getRequiredTugBoat(self):
        return self.requiredTugBoat
    def getTarget(self):
        return self.target
    def getStartTime(self):
        return self.startTime
    def getEndTime(self):
        return self.endTime
    def getAction(self):
        return self.action
    def getBerthId(self):
        return self.BerthId
    def setRequiredTugBoat(self,requiredTugBoat):
        self.requiredTugBoat=requiredTugBoat
    def setTarget(self,target):
        self.target=target
    def setStartTime(self,startTime):
        self.startTime=startTime
    def setEndTime(self,endTime):
        self.endTime=endTime
    def setAction(self,action="Enter"/"Out"):
        self.action=action
    def setBerthId(self,BerthId):
        self.BerthId=BerthId
    def __str__(self) -> str:
        return "requiredTugBoat:"+str(self.requiredTugBoat)+"\ntarget:"+str(self.target)+"\nstartTime:"+str(self.startTime)+"\nendTime:"+str(self.endTime)+"\naction:"+str(self.action)+"\nBerthId:"+str(self.BerthId)