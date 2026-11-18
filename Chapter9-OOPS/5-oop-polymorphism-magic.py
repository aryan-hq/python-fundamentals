# POLYMORPHISM AND DUNDER (MAGIC) METHODS

# Polymorphism means "many forms". It allows different classes to have methods 
# with the same name, or allows operators (like + or len()) to work on custom objects.

# 1. Duck Typing
# "If it walks like a duck and quacks like a duck, it's a duck."
# Python doesn't care what type an object is, only whether it has the required method.
class Dog:
    def speak(self): return "Woof!"

class Cat:
    def speak(self): return "Meow!"

# This function works for BOTH classes because they both have a 'speak' method.
def animal_sound(animal):
    print(animal.speak())

animal_sound(Dog())
animal_sound(Cat())


# 2. Dunder (Double Underscore) Methods / Magic Methods
# These special methods allow our custom objects to interact with built-in Python syntax.
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    # Defines what is printed when you do: print(my_book)
    # Without this, printing the object just shows its memory address: <__main__.Book object at 0x...>
    def __str__(self):
        return f"'{self.title}' by {self.author}"

    # Defines what happens when you do: len(my_book)
    def __len__(self):
        return self.pages

    # Operator Overloading: Defines what happens when you add two books together using '+'
    def __add__(self, other_book):
        # Let's say adding two books returns the combined total pages
        return self.pages + other_book.pages

    # You can read more about Emulating numeric types on : 
    # https://docs.python.org/3/reference/datamodel.html#emulating-numeric-types

book1 = Book("Python Crash Course", "Eric Matthes", 544)
book2 = Book("Clean Code", "Robert C. Martin", 464)

# Testing the Magic Methods
print(book1)                     # Triggers __str__
print("Pages:", len(book1))      # Triggers __len__
print("Total pages of both books:", book1 + book2) # Triggers __add__