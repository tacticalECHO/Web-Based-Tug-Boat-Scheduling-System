import User

class System_Administor(User.User):
    def __init__(self, name, password, System_AdministorId):
        super().__init__(name, password)
        self.name = name
        self.password = password
        self.System_AdministorId=System_AdministorId
    def getName(self):
        return self.name
    def getSystem_AdministorId(self):
        return self.System_AdministorId
    def setSystem_AdministorId(self, System_AdministorId):
        self.System_AdministorId=System_AdministorId
    def __str__(self) -> str:
        return super().__str__() + " System_AdministorId: " + str(self.System_AdministorId)