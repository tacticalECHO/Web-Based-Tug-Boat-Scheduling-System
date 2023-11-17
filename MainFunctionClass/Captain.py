import User 

class Captain(User.User):
    def __init__(self, name, password, CaptainId):
        super().__init__(name, password)
        self.name = name
        self.password = password
        self.CaptainId=CaptainId
    def getName(self):
        return self.name
    def getCaptainId(self):
        return self.CaptainId
    def setcaptainId(self, CaptainId):
        self.CaptainId=CaptainId
    def __str__(self) -> str:
        return super().__str__() + " CaptainId: " + str(self.CaptainId)
