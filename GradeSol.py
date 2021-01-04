#From Asma Emad to Everyone:  08:05 PM
# def a function that input student marks (unknown count) and then calculat avg,sum,grade

#userInput = input("Enter a comma-delimited list of numbers ")
#userList = userInput.split(",")
#try:
#    data_list = [float(number) for number in userList]
#except ValueError:
#    print("Please enter a comma-delimited list of numbers.")

x = 0
data_list = []
def grade(scores):
    if scores >= 90 and scores <= 100:
        return 'A'
    elif scores >= 80 and scores <= 89:
        return 'B'
    elif scores >= 70 and scores <= 79:
        return 'C'
    elif scores >= 60 and scores <= 69:
        return 'D'
    elif scores >= 50 and scores <= 59:
        return 'E'
    else:
        return 'F'
while x!="q":
    try:
        x = input("enter mark: ") #Error
        #x.isalpha()
        data_list.append(float(x))
    except ValueError:
        if x=="q":
            break
        


def list_modifier(list_var):
   print("Your list is: " + str(list_var))
   average = sum(list_var) / len(list_var)  # Divide list by sum of elements
   Sum =sum(list_var)
   Grade = grade(average)
   Result = "Average: {} Sum: {} Grade: {}".format(round(average,2),Sum,Grade)
   #Result = "Average: %s Sum: %s Grade: %s"%(average,Sum,Grade)
   #print("Average: " + str(average) + " Sum: "+ str(Sum) + " Grade: "+ str(Grade))
   print(Result)


list_modifier(data_list)
