# CLASSES, OBJECTS, AND THE '__init__' METHOD

# 1. What is a Class? What is an Object?
# A Class is a blueprint (like an architectural drawing of a house).
# An Object is the actual house built from that blueprint.
# You can build many houses (objects) from one drawing (class).

class Student:
    # 2. Class Attributes (Shared by ALL objects of this class)
    # If the university name changes, it changes for every student.
    university = "Delhi University"

    # 3. The __init__ Method (The Constructor)
    # This special method runs AUTOMATICALLY every time you create a new object.
    # It is used to initialize the specific data for that specific object.
    
    # 4. What is 'self'?
    # 'self' refers to the specific object being created right now. 
    # When creating Aryan, 'self.name' means "Aryan's name".
    def __init__(self, name, age, course):
        # Instance / object Attributes (Unique to each object)
        self.name = name
        self.age = age
        self.course = course

    # 5. Instance Methods
    # Functions defined inside a class are called "methods". 
    # They MUST have 'self' as their first parameter so they know which object they are working on.
    def introduce(self):
        return f"Hi, I'm {self.name}, studying {self.course}."

# 6. Creating Objects (Instantiation)
student1 = Student("Aryan", 20, "B. Tech")
student2 = Student("Sam", 19, "BSC")

# Accessing attributes and methods
print(student1.name)                     # Output: Aryan
print(student1.introduce())              # Output: Hi, I'm Aryan, studying BCA.
print(student2.introduce())              # Output: Hi, I'm Sam, studying B.Tech.

# Accessing the shared class attribute
print(f"{student1.name} goes to {student1.university}")
print(f"{student2.name} goes to {Student.university}") # Can be accessed via the Class directly