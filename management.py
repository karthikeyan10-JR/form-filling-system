import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="123456789",
  database="student_details")

obj=mydb.cursor()

def add():
    name = input("enter name:")
    branch = input("branch:")
    roll = input("roll:")
    section = input("section:")
    age = input("age:")
    insert = "insert into student(name,branch,roll,section,age)\
    values (%s, %s, %s, %s, %s)"
    val = (name,branch,roll,section,age)
    obj.execute(insert, val)
    mydb.commit()
    print("record inserted")


def update():
    roll_n=input("roll to update:")
    name = input("enter name:")
    branch = input("branch:")
    roll = input("roll:")
    section = input("section:")
    age = input("age:")
    Qry = ("UPDATE student SET name=%s,branch=%s,"\
    "roll=%s,section=%s,age=%s"\
    "WHERE roll=%s")
    val = (name,branch,roll,section,age,roll_n)
    obj.execute(Qry,val)
    mydb.commit()
    print("record updated")

def delete():
    obj=mydb.cursor()
    roll = input("roll no to delete:")
    su='''DELETE FROM STUDENT WHERE roll = %s'''
    deel=(roll,)
    obj.execute(su,deel)
    mydb.commit()
    print("record deleted")

def search():
    roll = input("enter rollto search:")
    qe="select * from student where roll = %s"
    se=(roll,)
    obj.execute(qe,se)
    r=obj.fetchone()
    print (r)



def mains():
    print("1.add")
    print("2.update")
    print("3.delete")
    print("4.search")
    option = int(input("enter the option:"))

    if (option == 1):
        add()
    elif (option ==2):
        update()
    elif (option == 3):
        delete()
    elif (option ==4):
        search()
    else:
        print("not recognised")
        
while 1==1:
    mains()
