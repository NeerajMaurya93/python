#Hinding the implementation details of a class and only showing the  essential features to the users
class Car:
    def __init__(self) -> None:
            self.acc=False
            self.brk=False
            self.clutch=False
    def start(self):
        self.clutch=True
        self.acc=True
        print("car started...")
car1=Car()
car1.start()