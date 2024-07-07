#!c:\Python\python.exe

import cgi
import mysql.connector

print("Content-Type:text/html\r\n\r\n")

Form=cgi.FieldStorage()

FFirstName=Form.getvalue('firstname')
FLastName=Form.getvalue('lastname')
FFatherName=Form.getvalue('fathername')
FMotherName=Form.getvalue('mothername')
FDateOfBirth=Form.getvalue('date')
FGender=Form.getvalue('gender')
FAddress=Form.getvalue('address')
FContact=Form.getvalue('contact')
FClasswantstoJoin=Form.getvalue('class')

print("<h1>Thank You For Registering!!!</h1>")
print("<h3>",FFirstName,FLastName,FFatherName,FMotherName,FDateOfBirth,FGender,FAddress,FContact,FClasswantstoJoin,"</h1>")

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="srcschool"
)

mycursor=mydb.cursor();

sql="INSERT INTO src(FirstName,LastName,FatherName,MotherName,DateOfBirth,Gender,Address,Contact,ClasswantstoJoin) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)";
val=(FFirstName,FLastName,FFatherName,FMotherName,FDateOfBirth,FGender,FAddress,FContact,FClasswantstoJoin)



mycursor.execute(sql,val)
mydb.commit()

print("</body>")
print("</html>")