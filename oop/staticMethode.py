#Methods that don't use the self parameter (work at class level)
class Student:
    def __init__(self,name,mark) -> None:
        self.name=name
        self.mark=mark
    @staticmethod#decorator
    def welcom():
        print("hello")
        # print("welcom students",self.name,self.mark)
    def get_mark(self):
        return self.mark
s1=Student("neeraj",78)
s1.welcom()
print(s1.get_mark())