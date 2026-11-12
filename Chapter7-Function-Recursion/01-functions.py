# A function is a block of reusable code that only runs when it is called.
# Python uses the 'def' keyword to define a function.

# 1. The Simplest Function
# Just defining the function name and what it does.
def say_hello():
    print("Hello there!")

say_hello() # Calling the function so it runs


# 2. Passing Arguments (Giving data to the function)
# Python is completely flexible. You just write a variable name inside the parentheses.
# Python doesn't care if you pass a string, a number, or an entire array into 'name'.
def greet_user(name):
    return f"Hello, {name}!"

print(greet_user("Aryan"))


# 3. Default Parameters
# If we call the function without providing an argument, it uses a default value.
def power(base, exponent=2):
    return base ** exponent

print("Square:", power(5))       # Uses default exponent (2) -> 25
print("Cube:", power(5, 3))      # Overrides default with 3 -> 125


# 4. Keyword Arguments
# You can send arguments with the 'key = value' syntax. 
# This way, you don't have to remember the exact order of the arguments.
def display_info(name, age, course):
    print(f"{name} is {age} years old, studying {course}.")

# Order doesn't matter because we specified the keys explicitly
display_info(course="BCA", name="Sam", age=20) 


# 5. Returning Multiple Values (Python "Cheat Code")
# Unlike C, which requires complex pointers or structs to return multiple things, 
# Python can return multiple values automatically. It packs them into a Tuple.
def get_min_max(numbers):
    return min(numbers), max(numbers) # Returns a tuple (min, max)

minimum, maximum = get_min_max([10, 20, 5, 40]) # Unpacking the tuple into variables
print(f"Min: {minimum}, Max: {maximum}")


# ADVANCED: 
# 6. Writing Professional Functions (Type Hints & Docstrings)

# In professional codebases, you will see extra syntax added to functions. 
# This doesn't change how the code runs, but it helps your code editor (like VS Code).

# A. Type Hints (: str and -> str)
# - name: str is just a sticky note saying: "Hey, I expect a string here."
# - -> str is a sticky note saying: "This function will spit out a string."
# Why use them? If you write this, and later accidentally pass an integer like greet_user_pro(100), 
# VS Code will put a warning line under it to help you catch bugs.

# B. Docstrings (""" ... """)
# A docstring (documentation string) is a multi-line comment placed immediately inside a function.
# Why not just use the # symbol? Because VS Code actively looks for these """ blocks. 
# If you write a docstring, whenever you hover your mouse cursor over 'greet_user_pro' 
# anywhere else in your file, VS Code pops up a little window displaying that exact text. 
# It creates a built-in mini instruction manual so you don't have to scroll up to remember how it works!

def greet_user_pro(name: str) -> str:
    """
    This is a docstring. It explains what the function does.
    Args: name (str): The name of the user.
    Returns: A greeting string.
    """
    return f"Hello, {name}!"

print(greet_user_pro("Aryan"))