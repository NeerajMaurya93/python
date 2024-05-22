#used to delete object properties or object itself
class Student:
    def __init__(self,name) -> None:
        self.name=name
s1=Student("neeraj")
print(s1.name)
del s1.ame
print(s1.name)