#!C:\Users\Hassan\AppData\Local\Programs\Python\Python38\python.exe

# Import modules for CGI handling 
import cgi, cgitb 
import mysql.connector

cnx = mysql.connector.connect(user='root', password='quark999',
	                          host='127.0.0.1',
	                          database='resort')


cursor = cnx.cursor()


# Create instance of FieldStorage 
form = cgi.FieldStorage() 

# Get data from fields
first_name = form.getvalue('first_name')
last_name  = form.getvalue('last_name')
if form.getvalue('gender'):
   gender = form.getvalue('gender')
else:
   gender = "Not set"

if form.getvalue('birth_day'):
   birth_day = form.getvalue('birth_day')
else:
   birth_day = "Not set"


if form.getvalue('check_in'):
   check_in = form.getvalue('check_in')
else:
   check_in = "Not set"

if form.getvalue('rate'):
   rate = form.getvalue('rate')
else:
   rate = "Not set"

if form.getvalue('room_no'):
   room_no = form.getvalue('room_no')
else:
   room_no = "Not set"

add_guest = ("INSERT INTO guest "
               "(birth_date, first_name, last_name, gender, room_no, check_in, rate) "
               "VALUES (%s, %s, %s, %s, %s, %s, %s)")
guest_data = (birth_day, first_name, last_name, gender, room_no, check_in, rate)
cursor.execute(add_guest, guest_data)

# Make sure data is committed to the database
cnx.commit()

cursor.close()
cnx.close()

print ("Content-type:text/html\r\n\r\n")
print ("<html>")
print ("<head>")
print ("<title>Hello - Second CGI Program</title>")
print ("</head>")
print ("<body>")
print ("Data Added : " , guest_data)
print("<br><br>")
print("<a href='http://127.0.0.1/cgi-bin/current_guests.py'> Current guest List </a>")
print ("</body>")
print ("</html>")

