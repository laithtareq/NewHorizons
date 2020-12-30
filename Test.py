# grade >> 100-90 A >> 90-80 B >> 

grade = float(input("Input grade: "))
def Mark(grade):
    if grade<=100 and grade>90:
        print("A")
    elif grade<=90 and grade>80:
        print("B")
    elif grade<=80 and grade>70:
        print("C")
    elif grade<=70 and grade>60:
        print("D")
    else: #grade 101 >> F
        print("F")
    
Mark(grade)