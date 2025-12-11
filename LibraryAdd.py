import mysql.connector
def addbook():
    try:
        con=mysql.connector.connect(host="localhost",
                               username="root",
                               passwd="mahesh1234",
                               database="libraryproject")
        cur=con.cursor()
        print("-"*50)
        bookno=int(input("Enter Book Number:"))
        bookname=input("Enter Book Name:")
        bookprice=float(input("Enter Book Price:"))
        bookpub=input("Enter Book Publication:")
        print("-"*50)
        lq="insert into library values(%d,'%s',%f,'%s')" %(bookno,bookname,bookprice,bookpub)
        cur.execute(lq)
        con.commit()
        print("{} Records Inserted Successfully--Verify".format(cur.rowcount))
    except mysql.connector.DatabaseError as db:
        print("Problem in Oracle:",db)
