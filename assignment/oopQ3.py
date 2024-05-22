class Employ:
    def __init__(self , role,dept,salary) -> None:
        self.role=role
        self.dept=dept
        self.salary=salary
    def sowDetails(self):
        print("role =",self.role)
        print("dept =",self.dept)
        print("salary =",self.salary)
        
class Engineer(Employ):
    def __init__(self,name,age):
        self.name=name
        self.age=age
        super().__init__("Engineer","IT","75,000")
        
engg1=Engineer("maurya ji","18")
engg1.sowDetails()
        
        