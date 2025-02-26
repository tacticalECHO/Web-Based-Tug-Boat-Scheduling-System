import Captain

class TugBoat():
    def __init__(self, boatID, currentBerthId, currentStatus="UNO") -> None:
        self.boatID = boatID
        self.currentStatus = currentStatus
        self.captain = Captain.Captain("UNO", "UNO")
        self.currentBerthId = currentBerthId
    def getBoatID(self):
        return self.boatID
    def getCurrentStatus(self):
        return self.currentStatus
    def getCaptain(self):
        return self.captain
    def getCurrentBerthId(self):
        return self.currentBerthId
    def setBoatID(self, boatID):
        self.boatID = boatID
    def setCurrentStatus(self, currentStatus):
        self.currentStatus = currentStatus
    def setCaptain(self, captain):
        self.captain = captain
    def setCurrentBerthId(self, currentBerthId):
        self.currentBerthId = currentBerthId
    def __str__(self) -> str:
        return "boatID:"+str(self.boatID)+"\ncurrentStatus:"+str(self.currentStatus)+"\ncaptain:"+str(self.captain)+"\ncurrentBerthId:"+str(self.currentBerthId)
    