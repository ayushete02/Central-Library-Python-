def Header():
    print("Books_Code\tBooks Name\n")


LibBooks = ["Coding Fundamentals", "Careers in Tech",
            "Clean Code", "Introduction to Algorithms", "The Art of Computer", "Blue DSA", "Code Complete", "C-programing", "Limiteness Mind", "Race to Developer", "Black Java", "Ultimate Programer", "HTML Style", "Red progamer", "Head First Python 3.0", "Python doc"]

if __name__ == "__main__":

    for book in LibBooks:
        print("📚", book)
