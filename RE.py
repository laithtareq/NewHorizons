import re
#Data = """Name : Laith Tareq
#Name : Ali Tareq"""
Data = open("Data.txt","r")
#if re.search("Name : ([A-Z a-z]+)",(Data.read())):
#    print("Found")
#Name = re.findall("Email : ([A-Z a-z]+@[A-Z a-z]+\.[A-Z a-z]{2,3})",(Data.read()))
#print(Name)
for line in Data:
    print(line)


# Data = open("Data.txt","w")  #H.W