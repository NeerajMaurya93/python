class Circle:
    def __init__(self,radius) -> None:
        self.radius=radius
        
    def area(self):
        return (22/7)*self.radius**2
    def perameter(self):
        return 2*(22/7)*self.radius
    
c1=Circle(4)

print(c1.area())
print(c1.perameter())
    