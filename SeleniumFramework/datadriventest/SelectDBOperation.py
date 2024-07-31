# insert , update, delete

import mysql.connector

try:
    con=mysql.connector.connect(host="localhost", port=3306, user="root", passwd="root", database="mydb")
    curs=con.cursor()  # create curosor
    curs.execute("select * from student")  #execute query through cursor

    for row in curs:
        print(row[0], row[1], row[2])

    con.close()  # close connection
except:
    print("Connection unsuccessful...")

print("Finished.....")