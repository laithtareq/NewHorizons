import sqlite3
import sys
import os
#os.makedirs("Data")
#db = sqlite3.connect("Data/Data.db")
db = sqlite3.connect("Data.db")
db.execute("create table if not EXISTS Address(firstName varchar,lastname varchar,address1 varchar,\
  address2 varchar,address3 varchar,address4 varchar,postcode varchar,stdCode varchar,telephone varchar)")
ans=True
while ans:
    print ("""
    1.Add New Address
    2.Change Existing Address
    3.View All Address Where the Last Name Starts With Letter
    4.List All Address
    5.Quit
    """)
    ans= input("Please Choose one of the above.. ") 
    if ans=="1": 
      print("\n Add New Address") 
      firstName = input("What is First name? ")
      lastname = input("What is Last Name ?")
      if (firstName == "" or lastname == ""): #\and
        print('No Name Added')
        break
      else :
        address1 = input("What Is Address1? ")
        address2 = input("What Is Address2? ")
        address3 = input("What Is Address3? ")
        address4 = input("What Is Address4? ")
        postcode = input("What Is Postcode? ")
        stdCode = input("What Is Stdcode? ")
        telephone = input("What Is Telephone? ")
        db.execute("insert into Address(firstName,lastname,address1,address2,address3,address4,postcode,stdCode,telephone) \
        values (?,?,?,?,?,?,?,?,?)",(firstName,lastname,address1,address2,address3,address4,postcode,stdCode,telephone))
        db.commit()
    elif ans=="2":
      print("\n Change Existing Address") 
      lastNameAddress = input("\n Please enter last name of address you want to change\n: ")
      lastNameFound = db.execute('select lastname from Address where lastname= ? ' ,(lastNameAddress,))
      #print(list(lastNameFound))
      if len(list(lastNameFound)) == 0: # may not work
        print("\n Lastname was NOT found. ") 
      else:
        newAddress1 = input("\n Please enter New Address1\n: ")
        newAddress2 = input("\n Please enter New Address2\n: ")
        newAddress3 = input("\n Please enter New Address3\n: ")
        newAddress4 = input("\n Please enter New Address4\n: ")
        newPostcode = input("\n Please enter New Postcode\n: ")
        newStdCode = input("\n Please enter New Stdcode\n: ")
        newTelephone = input("\n Please enter New Telephone\n: ")
        #sql = "update"
        L = []
        if newAddress1 != "":
            L.append("address1 = '{}' ".format(newAddress1))
        if newAddress2 != "":
            L.append("address2 = '{}' ".format(newAddress2))
        if newAddress3 != "":
            L.append("address3 = '{}' ".format(newAddress3))
        if newAddress4 != "":
            L.append("address4 = '{}' ".format(newAddress4))
        if newPostcode != "":
            L.append("postcode = '{}' ".format(newPostcode))
        if newStdCode != "":
            L.append("stdCode = '{}'".format(newStdCode))
        if newTelephone != "":
            L.append("telephone = '{}'".format(newTelephone))
        sql = ",".join(L)
        print(sql)
        In = "UPDATE Address SET {} \
           WHERE lastname = '{}' ".format(sql, lastNameAddress)
        print(In)
        db.execute("UPDATE Address SET {} \
           WHERE lastname = '{}' ".format(sql, lastNameAddress))
        db.commit() # was db.commit
    elif ans=="3":
      print("\n View All Address Where the Last Name Starts With Letter") 
      lastNameFirstLetter = input("\n Please enter the first letter of their last name ")
      addressData = db.execute("SELECT * FROM Address WHERE lastname LIKE ? ", (lastNameFirstLetter + "%",))
      for data in addressData:
        print(data)
    elif ans=="4":
      print("\n List All Address") 
      addressData = db.execute("select * from Address")
      for data in addressData:
        print(data)
    elif ans=="5":
      print("\n Goodbye") 
      sys.exit(-1)
    elif ans !="":
      print("\n input not recognised. please try again...") 