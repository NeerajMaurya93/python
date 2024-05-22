class Account:
    def __init__(self,acc_no,acc_pass) :
        self.__acc_no=acc_no#privet
        self.__acc_pass=acc_pass#privet
    def reset_pass(self):
        print(self.__acc_pass,self.__acc_no)        
acc1=Account("23453","@asdrgf")
print(acc1.reset_pass())