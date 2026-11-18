# INSTANCE, CLASS, AND STATIC METHODS

class Employee:
    company_name = "Google"
    raise_amount = 1.05 # 5% raise

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    # 1. Instance Method
    # Takes 'self' as the first argument. Works on specific object data.
    def apply_raise(self):
        self.salary = int(self.salary * self.raise_amount)

    # 2. Class Method (@classmethod)
    # Takes 'cls' (the class itself) as the first argument, NOT 'self'.
    # Used to modify class-level attributes that affect ALL objects.
    @classmethod
    def change_raise_amount(cls, amount):
        cls.raise_amount = amount

    # Class methods are also commonly used as "Alternative Constructors"
    @classmethod
    def from_string(cls, emp_str):
        # Parses a string like "John-50000" and creates an object
        name, salary = emp_str.split("-")
        return cls(name, int(salary))

    # 3. Static Method (@staticmethod)
    # Takes NEITHER 'self' nor 'cls'. It is just a regular function that is put 
    # inside the class because it makes logical sense for them to be grouped together.
    # It cannot modify object data or class data.
    @staticmethod
    def is_workday(day_string):
        if day_string == "Sunday" or day_string == "Saturday":
            return False
        return True

emp1 = Employee("Aryan", 100000)

# Using Class Method to change the raise amount for the whole company
Employee.change_raise_amount(1.10) # Now it's a 10% raise
emp1.apply_raise()
print(f"{emp1.name}'s new salary: {emp1.salary}")

# Using Alternative Constructor Class Method
emp2 = Employee.from_string("Jeff-75000")
print(f"Created from string: {emp2.name} makes {emp2.salary}")

# Using Static Method
print("Is Monday a workday?", Employee.is_workday("Monday"))