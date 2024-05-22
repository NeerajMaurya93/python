class Account:
    def __init__(self,ble,acc) -> None:
        self.balance=ble
        self.account_no=acc
    #debit methode
    def debit(self,amount):
        self.balance-=amount
        print("Rs",amount,"was debit",)
        print("total balance =",self.get_balance())
    #credit methode
    def credit(self,amount):
        self.balance+=amount
        print("Rs",amount,"was credit")
        print("total balance =",self.get_balance())
    def get_balance(self):
        return self.balance
acc1=Account(12000,365547856)
acc1.debit(3000)
acc1.credit(8000)
acc1.credit(4000)
