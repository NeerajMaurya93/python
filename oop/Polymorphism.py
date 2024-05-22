#when the same operator is allowed to have defferent meaning according to the context

# OPARETOR OVERLODING

# print(2+4) #3
# print(type(2))
# print("neeraj"+"maurya")#concatenate
# print(type("neeraj"))
# print([1,2,3]+[4,5,6,7])#merge
# print(type([1,2,3]))

class Complex:
    def __init__(self,real,img) -> None:
        self.real=real
        self.img=img
    def showNumber(self):
        print(self.real,"i +",self.img,"j")
    def __add__(self,num2):     #       note in this line use dendur function besase normal +not work without dendur function
        newReal=self.real+num2.real
        newImg=self.img+num2.img
        return Complex(newReal,newImg)
    def __sub__(self,num2):    
        newReal=self.real-num2.real
        newImg=self.img-num2.img
        return Complex(newReal,newImg)
num1=Complex(2,6)
num1.showNumber()
num2=Complex(3,8)
num2.showNumber()
#num3=num1.add(num2) #if we can not use add function then we can use dendur function(__add__,__sub__,__mult__)
num3=num1+num2
num3.showNumber()
num4=num1-num2
num4.showNumber()
