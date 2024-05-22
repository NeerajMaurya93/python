class Student:
    #defoult consturctor
    def __init__(self): 
        pass
    #parameterized constructor    
    def __init__(self,name,mark) -> None:
        self.name=name
        self.mark=mark
        # print("adding new student in database")
        
s1=Student("neeraj",78)
print(s1.name,s1.mark)
s2=Student("lucky",89)
print(s2.name,s2.mark)