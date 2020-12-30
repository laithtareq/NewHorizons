x = 5
y = 0
try:
    #print(X)
    #print(x/y)
    x.startswith()
except ZeroDivisionError:
    print('Error')
except NameError:
    print("Error 2")
except:
    print('Error 3')
finally:
    print("Final")