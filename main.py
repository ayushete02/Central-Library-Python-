from LibraryBooks import LibBooks
from LibraryBooks import Header
from playsound import playsound


def login(PerName, instruction):
    His = open("History.txt", "a")
    His.write(f"\n{PerName} {instruction}\n")
    His.close()


def line():
    print("_____________________________________________________________________________________________")


def BookHistory(PerName, Bookname, Note):
    His = open("History.txt", "a")
    His.write(
        f'''Name: {PerName}\t\t\t  Book Name: {Bookname}\t\t\t  Action: {Note} \n''')
    His.close()


def ClearHistory():
    Clr = open("History.txt", "w")
    Clr.write(f"History Clear by {PerName}\n")
    Clr.close()


def callClearHistory():
    playsound('.\Sounds\MouseClick.mp3 ')
    Fileopen = open("History.txt", "r")
    print(Fileopen.read())
    line()
    print("press 1 : Clear history\npress 2 : for return")
    clr = int(input('Enter your choice : '))
    if clr == 1:
        ClearHistory()
        playsound('.\Sounds\History.mp3 ')
        print("History Deleted Successfully")
        line()
    return True


class Library():
    def displayAvailableBooks(self):
        playsound('.\Sounds\MouseClick.mp3 ')
        print("\n==> Avaliable Books\n")
        Header()
        for index, Book in enumerate(LibBooks):
            print("   ", index+1100, "         ⨌  ", Book)
        line()
        return True

    def BorrowBooks(self, PerName, Bookname):

        if Bookname in LibBooks:
            print(
                f'\n==> Thanks for borrowing the book "{Bookname}", please keep it Safe and return within 30 Days'
            )
            playsound('.\Sounds\AddRemove.mp3 ')
            line()
            LibBooks.remove(Bookname)
            BookHistory(PerName, Bookname, "Borrow book")
            return True
        else:
            print("\n==> Sorry book is not Available in the Library")
            line()
            return True

    def ReturnBook(self, PerName, Bookname):
        print(f"Thanks for Returing the book - {Bookname}")
        LibBooks.append(Bookname)
        playsound('.\Sounds\AddRemove.mp3 ')
        line()
        BookHistory(PerName, Bookname, "Return/Add Book")
        return True


class Student():
    def BorrowBooks(self):
        Bookname = input("Enter name of the Book : ")
        playsound('.\Sounds\MouseClick.mp3 ')
        return Bookname

    def returnBook(self):
        Bookname = input("Enter name of the Book : ")
        playsound('.\Sounds\MouseClick.mp3 ')
        return Bookname


if __name__ == "__main__":

    # BookHistory("Ayush","C++","Borrrow Book")

    CentraLibrary = Library()
    Student = Student()
    PerName = input("Enter your Name (For Login): ")
    playsound('.\Sounds\MouseClick.mp3 ')
    login(PerName, "login")

    print('''\n⩩⩩ ⁂ ⁂  Welcome To the Central Library ⁂ ⁂ ⩩⩩ ''')

    while (True):
        playsound('.\Sounds\MouseClick.mp3 ')
        try:

            print('''
            Press 1 :  Check Available Books
            Press 2 :  Borrow Books
            Press 3 :  Add/Return Books
            Press 4 :  Exit Library 
            press 5 :  History
            ''')

            Input = int(input("Enter your Choice : "))
            playsound('.\Sounds\MouseClick.mp3 ')
            if Input == 1:
                CentraLibrary.displayAvailableBooks()
            elif Input == 2:
                CentraLibrary.BorrowBooks(PerName, Student.BorrowBooks())
            elif Input == 3:
                CentraLibrary.ReturnBook(PerName, Student.returnBook())
            elif Input == 4:
                login(PerName, "Logout")
                print("Thanks, Visit Again!!!\n\n#Created by : Ayush Shete")
                break
            elif Input == 5:
                callClearHistory()
            else:
                line()
                print("\n(❁ ❁ ❁ Invalid option Choose ❁ ❁ ❁")
                playsound('.\Sounds\Error.mp3 ')
                line()
                playsound('.\Sounds\MouseClick.mp3 ')
        except:
            line()
            print("\n❁ ❁ ❁ Invalid option Choose ❁ ❁ ❁")
            playsound('.\Sounds\Error.mp3 ')
            line()
            playsound('.\Sounds\MouseClick.mp3 ')

            #Created by : Ayush Shete #Python project
