import mysql.connector
def updatebook():
    try:
        con = mysql.connector.connect(host="localhost",
                                      username="root",
                                      passwd="mahesh1234",
                                      database="libraryproject")
        cur = con.cursor()
        print("-"*50)
        bookno = int(input("Enter Book Number for updating other details of Book:"))
        bookprice = float(input("Enter New Price:"))
        bookpub = input("Enter New Publication:")
        print("-" * 50)
        lq = "update library set price=%f, publication='%s' where bno=%d" %(bookprice,bookpub,bookno)
        cur.execute(lq)
        con.commit()
        if(cur.rowcount>0):
            print("{} Records Updated Successfully--Verify".format(cur.rowcount))
        else:
            print("Book Number does not exist")
    except mysql.connector.DatabaseError as db:
        print("Problem in Oracle:", db)

