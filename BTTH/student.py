from abc import ABC, abstractmethod

# Abstraction
class Display(ABC):
    @abstractmethod
    def show_info(self):
        pass


# Inheritance
class Person(Display):
    def __init__(self, id, name):
        self.id = id
        self.name = name


class Student(Person):
    def __init__(self, id, name, class_name):
        super().__init__(id, name)
        self.class_name = class_name

    # Polymorphism
    def show_info(self):
        print(f"{self.id} | {self.name} | {self.class_name}")