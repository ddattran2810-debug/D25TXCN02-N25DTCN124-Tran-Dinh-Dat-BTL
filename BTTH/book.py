from abc import ABC, abstractmethod

# Abstraction
class Display(ABC):
    @abstractmethod
    def show_info(self):
        pass


class Book(Display):
    def __init__(self, id, title, author, quantity):
        self.id = id
        self.title = title
        self.author = author

        # Encapsulation
        self.__quantity = quantity

    def get_quantity(self):
        return self.__quantity

    def borrow_book(self):
        if self.__quantity > 0:
            self.__quantity -= 1
            return True
        return False

    def return_book(self):
        self.__quantity += 1

    # Polymorphism
    def show_info(self):
        print(f"{self.id} | {self.title} | {self.author} | {self.__quantity}")

