class Student :
    def __init__(self,phy,chem,math) -> None:
        self.phy=phy
        self.chem=chem
        self.math=math
    @property
    def percentage(self):
        return str((self.phy+self.chem+self.math)/3)+"%"
stu1=Student(89,98,78)
print(stu1.percentage)
stu1.chem=86
print(stu1.percentage)
