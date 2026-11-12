import sys # imported built-in sys module (used in line 56)

# Recursion is when a function calls itself.
# EVERY recursive function must have two parts:
# 1. Base Case: The condition where the recursion stops.
# 2. Recursive Case: The condition where the function calls itself with a smaller input.

# Example 1: Factorial (5! = 5 * 4 * 3 * 2 * 1)
def factorial(n):
    # Base Case
    if n == 0 or n == 1:
        return 1
    # Recursive Case
    else:
        return n * factorial(n - 1)

print("Factorial of 5:", factorial(5))

# Example 2: Fibonacci Sequence (0, 1, 1, 2, 3, 5, 8...)
# Returning the nth Fibonacci number.
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        # Calls itself twice to add the two previous numbers
        return fibonacci(n - 1) + fibonacci(n - 2) 

print("7th Fibonacci number:", fibonacci(7))


# Recursion Limit in Python ------------
# Unlike loops, deep recursion takes up memory on the "Call Stack".

# 1. What is the "Call Stack"?
# Think of the Call Stack like a physical stack of sticky notes on your desk.
# When a function runs, Python writes its current progress on a sticky note.
# 
# In a normal loop (like a 'while' loop), Python uses the same sticky note 
# over and over, just erasing and updating the numbers. It takes up very little space.
#
# BUT in Recursion, a function calls a NEW version of itself before the first one finishes.
# Python has to pause the first function, grab a NEW sticky note, and put it on top 
# of the pile. If a function calls itself 500 times, you now have a pile of 500 sticky notes.

# 2. What is a "Stack Overflow"?
# In C, if you write infinite recursion, the program keeps stacking memory until 
# your computer forcefully kills it (this is the famous "Segmentation fault / core dumped").
# 
# Python is safer. It has a built-in ceiling. It says: 
# "I will only allow you to stack 1,000 sticky notes. If you try to place the 1,001st note, 
# I will stop the program and throw a 'RecursionError' to save your computer's memory."

# You can check your exact ceiling height using this:
print("Default recursion limit:", sys.getrecursionlimit()) # Usually outputs 1000

# 3. Why would we ever change it?
# When you practice advanced Data Structures and Algorithms (DSA), you will write 
# algorithms to search through massive "Trees" or "Graphs" (like a maze). 
# If the maze has 1,500 steps, your recursive function needs to call itself 1,500 times.
# 
# Python's default limit of 1000 will block you from solving the problem, even though 
# your logic is 100% correct.

# To bypass the safety net and raise the ceiling, you use:
# sys.setrecursionlimit(2000)

# WARNING: Only raise this limit when you absolutely have to. If your code has an 
# infinite recursion bug, raising this limit just delays the inevitable crash.