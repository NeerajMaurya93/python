#Methods are functions that belong to objects
class Student:
    def __init__(self,name,mark) -> None:
        self.name=name
        self.mark=mark
    def welcom(self):
        print("welcom students",self.name,self.mark)
    def get_mark(self):
        return self.mark
s1=Student("neeraj",78)
s1.welcom()
print(s1.get_mark())