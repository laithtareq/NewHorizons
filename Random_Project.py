import random,math
random.seed(1)
mark = 0
F = float(input("Enter the value of F: "))
x = random.randrange(1,100)
y = random.uniform(0,90)
z = x + random.uniform(0,10)
z = round(z,2)
A1 = float(input("what is value of A1 where x={},y={} degree,z={} ? ".format(x,y,z)))
A1_real = x*math.sin(math.degrees(y))
print(A1_real)
if A1_real-F<=A1 and A1_real+F>=A1:
    mark+=5
print(mark)
A2 = float(input("what is value of A2 where x={},y={} degree,z={} ? ".format(x,y,z)))
A2_real = z-A1*(x+math.cos(math.degrees(y)))
print(A2_real)
if A2_real-F<=A2 and A2_real+F>=A2:
    mark+=5
print(mark)
