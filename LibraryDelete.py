import mysql.connector
def deletebook():
    try:
        con = mysql.connector.connect(host="localhost",
                                      username="root",
                                      passwd="mahesh1234",
                                      database="libraryproject")
        cur=con.cursor()
        print("-"*50)
        empno=int(input("Enter Book Number:"))
        dq="delete from library where bno=%d" %empno
        cur.execute(dq)
        con.commit()
        if(cur.rowcount>0):
            print("{} Book Deleted From Library--Verify".format(cur.rowcount))
        else:
            print("Book Number Does Not Exist")
    except mysql.connector.DatabaseError as db:
        print("Problem in Oracle:",db)
