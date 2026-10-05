import mysql.connector

con=mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password"
    database="SMS_Demo"
)
print("database created successfully")

my_cursor=con.cursor()

my_cursor.execute("create table Students(ROLLNO INT PRIMARY KEY,NAME VARCHAR (100) not null,MOBILENO varchar(15) unique,CITY VARCHAR(50),COURSE VARCHAR(50))")
print("TABLE CREATED SUCCESSFULLY")

def add_details():
    rollno=int(input("Enter ROLLNO : "))
    name=input("Enter Name : ")
    mobileno=input("Enter Mobile Number : ")
    city=input("Enter City : ")
    course=input("Enter Course : ")
    query="insert into students values (%s,%s,%s,%s,%s)"
    values=(rollno,name,mobileno,city,course)
    my_cursor.execute(query,values)
    con.commit()
    print("Student Added Successfully")

def update_details():
    name=input("Enter Name : ")
    mobileno=input("Enter Mobile Number : ")
    city=input("Enter City : ")
    course=input("Enter Course : ")
    rollno=int(input("Enter ROLLNO : "))
    query="update students set name=%s,mobileno=%s,city=%s,course=%s where rollno=%s"
    values=(name,mobileno,city,course,rollno)
    my_cursor.execute(query,values)
    con.commit()
    print("Student Detail Updated Successfully")

def view_all():
    my_cursor.execute("select * from students")
    result=my_cursor.fetchall()
    for row in result:
        print(row)

def delete_student_details():
    rollno=int(input("Enter Rollno to delete : "))
    query="delete from students where rollno=%s"
    values=(rollno,)
    my_cursor.execute(query,values)
    con.commit() 
    print("Student Deleted Successfully")


print(" ENTER 1 for ADD Student\n ENTER 2 for UPDATE Student Detail\n ENTER 3 for VIEW ALL Student Detail\n ENTER 4 to DELETE Student from Record\n ENTER 5 to EXIT")

while True:
    print("ENTER 1 for ADD Student")
    print("ENTER 2 for UPDATE Student Detail") 
    print("ENTER 3 for VIEW ALL Student Detail") 
    print("ENTER 4 to DELETE Student from Record")
    print("ENTER 5 to EXIT")
    choice=int(input("Select From Menu : "))
    if choice ==1:
        add_details()
        break

    elif choice ==2:
        update_details()
        break 

    elif choice ==3:
        view_all()
        break

    elif choice ==4:
        delete_student_details()
        break

    elif choice ==5:
        print("5.EXIT")
        break

    else:
        print("Invalid choice")

con.close()