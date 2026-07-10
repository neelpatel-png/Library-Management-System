print("-----------------------------------------")
print("    WELCOME TO LIBRARY MANAGMENT SYSTEM    ")
print("-----------------------------------------")

library = {}
with open("books.txt") as file:
                    for line in file:
                        name,status = line.strip().split(",")
                        library[name.strip()] = status.strip()

def menu():
        print()
        print("---------------------")
        print("         MENU        ")
        print("---------------------")
        print()
        print("1. ADD BOOK")
        print("2. VIEW BOOKS")
        print("3. SEARCH BOOK")
        print("4. BORROW BOOK")
        print("5. RETURN BOOK")
        print("6. EXIT")
        print()

def save_library():
    with open("books.txt", "w") as file:
        for book in library:
            file.write(f"{book},{library[book]}\n")

def func_add():
            print()
            print("-------------------------------")
            print("       ADD BOOK      ")
            print("-------------------------------")
            print()
            book_name = input("Enter Name of Book to ADD : ")
            if book_name in library:
                print("Book already Exists in the Library")
            else:
                library[book_name] = "Available"
                save_library()
                print("Book has been added to the library succesfuly")

def func_view():
    print()
    print("-------------------------------")
    print("        VIEW ALL BOOKS         ")
    print("-------------------------------")
    print()
    for name in library:
        print(f"name : {name}")
        print(f"status : {library[name]}")
        print()

def func_search():
    print()
    print("-------------------------------")
    print("          SEARCH BOOK          ")
    print("-------------------------------")
    print()
    search_id = input("Enter name of book to search : ")
    if search_id in library:
        print()
        print("Book Found!")
        print()
        print(f"Name : {search_id}")
        print(f"Status : {library[search_id]}")
    else:
        print()
        print("No such book in the library")

def func_borrow():
    print()
    print("----------------------------")
    print("         BORROW BOOK        ")
    print("----------------------------")
    print()
    borrow_id = input("Enter name of the book that is to be borrowed : ")
    if borrow_id in library:
        if library[borrow_id] == "Available":
            library[borrow_id] = "Borrowed"
            save_library()
            print()
            print("Book issued successfully")
        else:
            print()
            print("This Book has already been borrowed please wait for it to be returned")
    else:
        print()
        print("No such book exists in the library")

def func_return():
    print()
    print("----------------------------")
    print("         RETURN BOOK        ")
    print("----------------------------")
    print()
    return_id = input("Enter name of the book that has to be returned : ")
    if return_id in library:
        if library[return_id] == "Borrowed":
            library[return_id] = "Available"
            save_library()
            print()
            print("Book returned successfully")
        else:
            print()
            print("This book is already available in the library")
    else:
        print()
        print("Such book does not exist in the library")
        ask = input("would you like to add this book to the library? : ")
        ask = ask.lower()
        if ask == "yes":
            func_add()
        else:
            print()
            print("This book can't be returned")

while True:
    menu()
    try:
        choice = int(input("Enter your choice : "))
    except ValueError:
        print("Enter a Valid Choice")
    else:
        if choice == 1:
            func_add()
        elif choice == 2:
            func_view()
        elif choice == 3:
            func_search()
        elif choice == 4:
            func_borrow()
        elif choice == 5:
            func_return()
        elif choice == 6:
            print()
            print("---------------------------------------------------------")
            print("         THANK YOU FOR USING LIBRARY MANAGEMENT SYSTEM     ")
            print("---------------------------------------------------------")
            break
        else:
            print()
            print("Enter a valid choice from above given options")
            print()