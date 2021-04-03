#!C:\Users\Hassan\AppData\Local\Programs\Python\Python38\python.exe

import mysql.connector

cnx = mysql.connector.connect(user='root', password='quark999',
	                          host='127.0.0.1',
	                          database='resort')

cursor = cnx.cursor()

query = ("SELECT guest_id, first_name , last_name, gender, room_no, check_in,  rate from guest where check_out is null")


cursor.execute(query)
#guest_id, first_name, last_name, gender, room_no, check_in, check_out,  rate
print ("Content-type:text/html\r\n\r\n")
print ("<html>")
print ("<head>")
print ("<title>Hello - Second CGI Program</title>")
style = """<style>
table, th, td {
  border: 1px solid black;
  border-collapse: collapse;
}
th, td {
  padding: 10px;
}  
</style>"""
print(style)
print ("</head>")
print ("<body>")
tableStr = """
<table>
<thead>
  <tr>
    <th>id</th>
    <th>First Name</th>
    <th>Last Name</th>
    <th>Gender</th>
    <th>Room No</th>
    <th>Check in</th>
    <th>Rate</th>
  </tr>
</thead>
<tbody>"""
print(tableStr)
for (guest_id, first_name , last_name, gender, room_no, check_in, rate) in cursor:
	print("<tr>")
	print("<td>",guest_id,"</td>","<td>",first_name,"</td>", "<td>",last_name,"</td>", "<td>",gender,"</td>", "<td>",room_no,"</td>", "<td>",check_in,"</td>", "<td>",rate,"</td>")
	print("</tr>")

print("</tbody>")
print("</table>")

print ("</body>")
print ("</html>")


cursor.close()
cnx.close()


