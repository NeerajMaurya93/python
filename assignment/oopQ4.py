class Order:
    def __init__(self,item,price):
        self.item=item
        self.price=price
    def __gt__(self,odr2):
        return self.price>odr2.price
odr1=Order("mango","30")
odr2=Order("tea","15")
print(odr1 > odr2)#true