import oracledb as orc
def viewemp():
    try:
        con = orc.connect("system/maahi7674@localhost/orcl.bbrouter")
        cur = con.cursor()
        print("-"*50)
        sq="select * from employee02 where eno={}".format(int(input("Enter Employee Number:")))
        cur.execute(sq)
        print("-"*50)
        record=cur.fetchone()
        if(record==None):
            print("Employee Does NOt Exist")
        else:
            print("Employee NUmber:{}".format(record[0]))
            print("Employee Name:{}".format(record[1]))
            print("Employee Salary:{}".format(record[2]))
            print("Employee Compony:{}".format(record[3]))
    except orc.DatabaseError as db:
        print("Problem in Oracle:",db)
def viwallemp():
    try:
        con = orc.connect("system/maahi7674@localhost/orcl.bbrouter")
        cur = con.cursor()
        sq="select * from employee02"
        cur.execute(sq)
        print("-"*50)
        for cal in cur.description:
            print(cal[0],end="\t\t")
        print()
        print("-"*50)
        records=cur.fetchall()
        for record in records:
            for val in record:
                print(val,end="\t\t")
            print()
    except orc.DatabaseError as db:
        print("Problem in oracle:",db)

