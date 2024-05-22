# super() method is used to access methode of the parent class

class Car:
    def __init__(self,type) -> None:
        self.type=type
    @staticmethod
    def start():
        print("car started")
    @staticmethod
    def stop():
        print("car stoped")
class toyotaCar(Car):
    def __init__(self,name,type) -> None:
        self.name=name

        #self.type=type#type is only avalble for the toypta but nat parent class ,, if we want to geven type to parent class then we use the super method
        super().__init__(type)
        self.name=name
        super().start()
car1=toyotaCar("prius","electric")
print(car1.type)