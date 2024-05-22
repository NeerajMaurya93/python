#when one class derives the properties & methods of another class

#single inheritance

class Car:
    color="black"
    @staticmethod
    def start():
        print("car started")
    @staticmethod
    def stop():
        print("car stoped")
class toyotaCar(Car):
    def __init__(self,name) -> None:
        self.name=name
car1=toyotaCar("fortuner")
print(car1.name)
print(car1.start())
print(car1.color)

#multi_level inheritance

class Car:
    @staticmethod
    def start():
        print("car started")
    @staticmethod
    def stop():
        print("car stoped")
class toyotaCar(Car):
    def __init__(self,brand) -> None:
        self.brand=brand
class Fortuner(toyotaCar):
    def __init__(self,type) -> None:
        self.type = type
car1=Fortuner("disel")
print(car1.type)
car1.start()

# multiple inheritance

class A():
    varA="welcome to class A"
class B():
    varB="welcome to class B"
class C(A,B):
    varC="welcome to class C"
c1=C()
print(c1.varC)
print(c1.varB)
print(c1.varA)

