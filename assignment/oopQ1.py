class Mark:
    def __init__(self,name,mark) -> None:
            self.name=name
            self.mark=mark
    def get_avg(self):
        sum=0
        for value in self.mark:
            sum=sum+value
        print("he",self.name,"your avg markis  is :",sum/3)
s1=Mark("neeraj maurya",[89,78,69])
s1.get_avg()
s1.name="lucky"
s1.get_avg()