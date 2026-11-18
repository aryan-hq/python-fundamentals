# ABSTRACTION AND ABSTRACT BASE CLASSES (ABC)

# Abstraction hides complex background details and shows only the essential features.
# An Abstract Class is a template that CANNOT be instantiated on its own. 
# It exists purely to force its child classes to implement specific methods.

from abc import ABC, abstractmethod

# 1. Creating the Abstract Base Class
class Shape(ABC): # Inheriting from ABC makes this an abstract class
    
    @abstractmethod
    def calculate_area(self):
        # This method is empty. Every child class MUST write their own version of this.
        pass

# shape = Shape() # THIS WILL CRASH! You cannot create an object from an Abstract Class.

# 2. Creating Child Classes
class Square(Shape):
    def __init__(self, side):
        self.side = side

    # If we do not write this calculate_area method, Python will crash when we try to create a Square.
    def calculate_area(self):
        return self.side * self.side

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius * self.radius

# Now we can safely create the child objects
my_square = Square(4)
my_circle = Circle(5)

print(f"Square Area: {my_square.calculate_area()}")
print(f"Circle Area: {my_circle.calculate_area()}")