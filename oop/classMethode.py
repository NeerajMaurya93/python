class Person:
    name="anonymous"
    # def chengeName(self,name):
        # self.name=name  #or
        # self.__class__.name=name  #or
       # Person.name=name  #or          #if we replace the self .name withe the Person .name then aoutput same
    @classmethod
    def chengeName(cls,name):
       cls.name=name
p1=Person()
p1.chengeName("neeraj")
print(p1.name)
print(Person.name)

    