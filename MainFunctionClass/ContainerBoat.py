
class ContainerBoat:
    def __init__(self) -> None:
        self.containerBoatID=""
        self.tonnage=0
        self.country=""
        self.arrivalTime=""
        self.leaveTime=""
    def getContainerBoatID(self):
        return self.containerBoatID
    def getTonnage(self):
        return self.tonnage
    def getCountry(self):
        return self.country
    def getArrivalTime(self):
        return self.arrivalTime
    def getLeaveTime(self):
        return self.leaveTime
    def setContainerBoatID(self,containerBoatID):
        self.containerBoatID=containerBoatID
    def setTonnage(self,tonnage):
        self.tonnage=tonnage
    def setCountry(self,country):
        self.country=country
    def setArrivalTime(self,arrivalTime):
        self.arrivalTime=arrivalTime
    def setLeaveTime(self,leaveTime):
        self.leaveTime=leaveTime
    def __str__(self) -> str:
        return "containerBoatID:"+str(self.containerBoatID)+"\ntonage:"+str(self.tonnage)+"\ncountry:"+str(self.country)+"\narrivalTime:"+str(self.arrivalTime)+"\nleaveTime:"+str(self.leaveTime)
