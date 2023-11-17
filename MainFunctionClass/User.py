from abc import ABC, abstractmethod

class User(ABC):
    def __init__(self, name, password):
        self.name = name
        self.password = password
    @abstractmethod
    def getName(self):
        return self.name
    @abstractmethod
    def getPassword(self):
        return self.password
    @abstractmethod
    def __str__(self) -> str:
        return super().__str__() + " name: " + str(self.name) + " password: " + str(self.password)