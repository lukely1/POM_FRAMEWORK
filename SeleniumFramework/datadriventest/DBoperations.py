# insert, update, delete

insert_query = "INSERT INTO STUDENT VALUES(104, 'Luke', 100)"
update_query = "update student set SNAME='Mary' where SNO = 104;"
delete_query = "delete from student where SNO=104"

import mysql.connector


try:
    con = mysql.connector.connect(host="localhost", port=3306, user="root", passwd="root", database="mydb")
    curs = con.cursor()  # create curosor
    curs.execute(delete_query)  #execute query through cursor
    con.commit()  # commit transaction
    con.close()
except:
    print("Connection unsuccessful...")

print("Finished.....")
