from book import Book
from student import Student


class Library:
    def __init__(self):
        self.books = []
        self.students = []

    # ================= BOOK =================

    def add_book(self):
        book_id = input("Nhập mã sách: ")
        title = input("Nhập tên sách: ")
        author = input("Nhập tác giả: ")

        while True:
            try:
                quantity = int(input("Nhập số lượng: "))

                if quantity < 0:
                    print("Số lượng không được âm!")
                else:
                    break

            except ValueError:
                print("Vui lòng nhập số!")

        book = Book(book_id, title, author, quantity)
        self.books.append(book)

        print("Thêm sách thành công!")

    def view_books(self):
        if not self.books:
            print("Danh sách sách trống!")
            return

        for book in self.books:
            book.show_info()

    def search_book(self):
        book_id = input("Nhập mã sách: ")

        for book in self.books:
            if book.id == book_id:
                print("Đã tìm thấy sách:")
                book.show_info()
                return

        print("Book not found!")

    def delete_book(self):
        book_id = input("Nhập mã sách cần xóa: ")

        for book in self.books:
            if book.id == book_id:
                self.books.remove(book)
                print("Xóa sách thành công!")
                return

        print("Book not found!")

    # ================= STUDENT =================

    def add_student(self):
        student_id = input("Nhập mã sinh viên: ")
        name = input("Nhập họ tên: ")
        class_name = input("Nhập lớp: ")

        student = Student(student_id, name, class_name)

        self.students.append(student)

        print("Thêm sinh viên thành công!")

    def view_students(self):
        if not self.students:
            print("Danh sách sinh viên trống!")
            return

        for student in self.students:
            student.show_info()

    def search_student(self):
        student_id = input("Nhập mã sinh viên: ")

        for student in self.students:
            if student.id == student_id:
                print("Đã tìm thấy sinh viên:")
                student.show_info()
                return

        print("Student not found!")

    def delete_student(self):
        student_id = input("Nhập mã sinh viên cần xóa: ")

        for student in self.students:
            if student.id == student_id:
                self.students.remove(student)
                print("Xóa sinh viên thành công!")
                return

        print("Student not found!")

    # ================= BORROW =================

    def borrow_book(self):
        student_id = input("Nhập mã sinh viên: ")
        book_id = input("Nhập mã sách: ")

        student = None
        book = None

        for s in self.students:
            if s.id == student_id:
                student = s
                break

        if student is None:
            print("Student not found!")
            return

        for b in self.books:
            if b.id == book_id:
                book = b
                break

        if book is None:
            print("Book not found!")
            return

        if book.borrow_book():
            print("Mượn sách thành công!")
        else:
            print("Sách đã hết!")

    # ================= RETURN =================

    def return_book(self):
        book_id = input("Nhập mã sách trả: ")

        for book in self.books:
            if book.id == book_id:
                book.return_book()
                print("Trả sách thành công!")
                return

        print("Book not found!")