class Math:
    def __init__(self,**kwargs):
        self.x = kwargs["x"]
        self.y = kwargs["y"]
    def Sum(self):
        return self.x +self.y
    def Sub(self):
        return self.x-self.y
    def Mul(self,z):
        return self.x*self.y*z
class Student:
    def __init__(self,**kwargs):
        self.Name = ""
        self.M = []
    def Marks(self):

    def Grade(self):
        
        self.M
        return G
#X = Math.Sum(1,2)
#X = Math.Sub(1,2)
X = Math(x=1,y=2) # kwargs = {"x":1,"Y":2}
print(X.Sum())
print(X.Mul(2))
S = Student()
S.marks()
