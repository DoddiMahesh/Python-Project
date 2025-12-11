import mysql.connector
def viewbook():
    try:
        con = mysql.connector.connect(host="localhost",
                                      username="root",
                                      passwd="mahesh1234",
                                      database="libraryproject")
        cur=con.cursor()
        print("-"*50)
        bookno=int(input("Enter Book Number to View its Details:"))
        vq="select * from library where bno=%d" %(bookno)
        cur.execute(vq)
        record=cur.fetchone()
        if(record==None):
            print("Book Does NOt Exist")
        else:
            print("Book Number:{}".format(record[0]))
            print("Book Name:{}".format(record[1]))
            print("Book Price:{}".format(record[2]))
            print("Book Publication:{}".format(record[3]))

    except mysql.connector.DatabaseError as db:
        print("Problem in Oracle:",db)



def viewallebooks():
    try:
        con = mysql.connector.connect(host="localhost",
                                      username="root",
                                      passwd="mahesh1234",
                                      database="libraryproject")
        cur=con.cursor()
        print("-"*50)
        vq="select * from library"
        cur.execute(vq)
        for col in cur.description:
            print(col[0],end="\t")
        print("-"*50)
        records=cur.fetchall()
        for record in records:
            for val in record:
                print(val,end="\t")
            print()

    except mysql.connector.DatabaseError as db:
        print("Problem in Oracle:",db)


