# 1. Scope (Local vs Global)
# Variables created inside a function are LOCAL. 
# Variables created outside all functions are GLOBAL.

message = "I am Global"

def test_scope():
    message = "I am Local" # This creates a NEW local variable, it doesn't change the global one.
    print("Inside function:", message)

test_scope()
print("Outside function:", message)

# The 'global' keyword
# If you actually need to modify a global variable from inside a function:
counter = 0

def increment():
    global counter # Tells Python: "Use the counter from the global scope"
    counter += 1

increment()
print("Counter is now:", counter)


# 2. Lambda Functions (Anonymous Functions)
# A lambda function is a small, one-line function without a name.
# Syntax: lambda arguments : expression

# Standard function
def square(x):
    return x ** 2

# Equivalent Lambda function
square_lambda = lambda x : x ** 2
print("Lambda Square:", square_lambda(6))

# WHY USE LAMBDAS? 
# They are incredibly useful for sorting complex data structures (like dictionaries or lists of tuples) 
# which you will do a lot in LeetCode.

students = [("Sam", 85), ("Jeff", 92), ("Musk", 78)]
# Sort the list based on the SECOND item in each tuple (the score)
students.sort(key=lambda student: student[1]) 
print("Sorted students by score:", students)