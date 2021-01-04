List1 = [1,2,4,4,7,8,8]
List2 = [1,3,4,4,7,8,8]
print(list(set(List1)-set(List2))+list(set(List2)-set(List1)))
#print(set(List))