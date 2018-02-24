class Person:
    def __init__(self):
        print("class created")

    def setName(self,firstName,lastName):
        self.firstName=firstName
        self.lastName=lastName

    def printName(self):
        print(self.firstName,self.lastName)

    def __del__(self):
        print("class detroyed")
        
person_=Person()
person_.setName("Evashen","Naicker")
person_.printName()
