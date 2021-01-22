def show_menu():
    choice = input("""     Main Menu
    1) Add new Address
    2) Existing Address
    3) Veiw all Address where lastname start with letter
    4) List All Address
    5) Quit
    """)
    try:
        choice = int(choice)
    except:
        choice = 0
    return choice
def new_address():
    data = {}
    Add = True
    data["firstname"] = input("Enter firstname: ")
    if data["firstname"] == "":
        Add = False
        print("No Name Added")
        return data,Add
    data["lastname"] = input("Enter lastname: ")
    if data["lastname"] == "":
        Add = False
        print("No Name Added")
        return data,Add
    data["address1"] = input("Enter address1: ")
    data["address2"] = input("Enter address2: ")
    data["address3"] = input("Enter address3: ")
    data["address4"] = input("Enter address4: ")
    data["postcode"] = input("Enter postcode: ")
    data["stdCode"] = input("Enter stdCode: ")
    data["telephone"] = input("Enter telephone: ")
    return data,Add
def change_address(old_Data):
    new_data = {}
    lastname_List = []
    lastname = input("Enter lastname to be changed: ")
    for data in old_Data:
        lastname_List.append(data["lastname"])
    if lastname in lastname_List:
        new_data["address1"] = input("Enter address1: ")
        new_data["address2"] = input("Enter address2: ")
        new_data["address3"] = input("Enter address3: ")
        new_data["address4"] = input("Enter address4: ")
        new_data["postcode"] = input("Enter postcode: ")
        new_data["stdCode"] = input("Enter stdCode: ")
        new_data["telephone"] = input("Enter telephone: ")
        for data in old_Data: # old_Data = [{},{},{},...]
            # data = {"lastname":"....","firstname":"....",.....}
            if data['lastname'] == lastname:
                data['address1'] = new_data["address1"]
                data['address2'] = new_data["address2"]
                data['address3'] = new_data["address3"]
                data['address4'] = new_data["address4"]
                data["postcode"] = new_data["postcode"]
                data["stdCode"] = new_data["stdCode"]
                data["telephone"] = new_data["telephone"]
    else:
        print("lastname is not correct")
    return old_Data
def view_lastname(old_Data):
    firstletter = input("Enter first letter of lastname: ")
    for data in old_Data:
        if data["lastname"].startswith(firstletter):
            print("firstname: {}".format(data["firstname"]))
            print("lastname: {}".format(data["lastname"]))
            print("address: {}".format(data["address1"]))
            print("         {}".format(data["address2"]))
            print("         {}".format(data["address3"]))
            print("         {}".format(data["address4"]))
            print("postcode: {}".format(data["postcode"]))
            print("stdCode: {}".format(data["stdCode"]))
            print("telephone: {}".format(data["telephone"]))
def view_all(old_Data):
    for data in old_Data:
        print("firstname: {}".format(data["firstname"]))
        print("lastname: {}".format(data["lastname"]))
        print("address: {}".format(data["address1"]))
        print("         {}".format(data["address2"]))
        print("         {}".format(data["address3"]))
        print("         {}".format(data["address4"]))
        print("postcode: {}".format(data["postcode"]))
        print("stdCode: {}".format(data["stdCode"]))
        print("telephone: {}".format(data["telephone"]))
def Save_Data(Data):
    File = open("Data.txt","w")
    Data = str(Data)
    File.write(Data)

choice = show_menu()
Data = []   #Data = [{"firstname":"...","lastname":"..."},{},{}....]
while choice != 5:
    if choice not in [1,2,3,4]:
        print("input not recognised. please try again...")
    elif choice == 1:
        data,Add = new_address() # data = {"firstname":"...","lastname":"..."}
        if Add:
            Data.append(data)
    elif choice == 2:
        Data = change_address(Data) # Will back
    elif choice == 3:
        view_lastname(Data)
    elif choice == 4:
        view_all(Data)
    choice = show_menu()
Save_Data(Data)


