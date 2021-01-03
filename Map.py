import timeit
setup1 = """
X = [1,2,3,4,5]
Y = [4,2,6,4,7]
Z = []
Sum = lambda x,y:x+y
for i in range(len(X)):
    Z.append(Sum(X[i],Y[i]))
"""
#print(timeit.timeit(setup1,number=10000))


X = [1,2,3,4,5]
Y = [4,2,6,4,7]
W = [4,2,6,4,7]
Z = list(map(lambda x,y,w=2:x+y+w,X,Y,W))
print(Z)
#print(timeit.timeit(setup2,number=10000))