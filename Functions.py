#print(max("Hello word"))
#print(min("Hello Word"))
import math
import random
# D = R*180/(22/7)
#print(math.sin(math.degrees(30)))

#print(random.random())
#print(random.randrange(2,8))
#print(random.choice([2,3,8]))
#print(random.uniform(2,8))
#print(dir(random))
x = 2
y = 4
def FunName(x,y,z=2):
    Sum = x+y+z
    return Sum
Sum = FunName(x,y)
print(Sum)