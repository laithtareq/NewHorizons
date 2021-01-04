import sqlite3
db = sqlite3.connect("Data.db")

db.execute("delete from Student")
db.execute("delete from Mat_tbl")

db.execute("create table if not EXISTS Student(Name varchar,Class char,ID INT)")
db.execute("insert into Student(Name,ID) values (?,?)",("Ali",1))
db.execute("insert into Student(Name,ID) values (?,?)",("Asma",2))
#sql = "insert into Student(Name,ID) values ('{}',{})".format("Ali",1)
#db.execute(sql)
db.execute("create table if not EXISTS Mat_tbl(Mat varchar)")
db.execute("insert into Mat_tbl(Mat) values (?)",("Math",))
db.commit()
Data = db.execute("select * from Student")
for data in Data:
    print(data)
db.execute("create view St_View as select Name,ID from Student")


