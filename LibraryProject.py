from LibrayMenu import bookmenu
from LibraryAdd import addbook
from LibraryDelete import deletebook
from LibraryUpdate import updatebook
from LibraryView import viewbook, viewallebooks
while(True):
    try:
        print("-" * 50)
        bookmenu()
        ch=int(input("Enter your choice:"))
        match(ch):
            case 1:
                addbook()
            case 2:
                deletebook()
            case 3:
                updatebook()
            case 4:
                viewbook()
            case 5:
                viewallebooks()
            case 6:
                print("THANKS FOR USING THIS PROJECT")
                break
            case _:
                print("\tYOUR SELECTION OF OPERATION IS WRONG--TRY AGAIN")
    except ValueError:
        print("\tDONT ENTER ALNUMS,STRS AND SYMBOLS FOR CHOICE--TRY AGAIN")
