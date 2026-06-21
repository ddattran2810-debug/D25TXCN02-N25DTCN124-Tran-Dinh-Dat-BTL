from library import Library
library = Library()

while True:
    print("\n========== LIBRARY MANAGEMENT ==========")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Delete Book")
    print("5. Add Student")
    print("6. View Students")
    print("7. Search Student")
    print("8. Delete Student")
    print("9. Borrow Book")
    print("10. Return Book")
    print("0. Exit")

    choice = input("Nhập lựa chọn: ")

    if choice == "1":
        library.add_book()

    elif choice == "2":
        library.view_books()

    elif choice == "3":
        library.search_book()

    elif choice == "4":
        library.delete_book()

    elif choice == "5":
        library.add_student()

    elif choice == "6":
        library.view_students()
    elif choice == "7":
        library.search_student()

    elif choice == "8":
        library.delete_student()

    elif choice == "9":
        library.borrow_book()

    elif choice == "10":
        library.return_book()

    elif choice == "0":
        print("Thoát chương trình!")
        break

    else:
        print("Lựa chọn không hợp lệ!")