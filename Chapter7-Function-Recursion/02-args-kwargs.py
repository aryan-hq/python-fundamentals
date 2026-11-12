# Sometimes you don't know how many arguments will be passed into your function.
# Python handles this using *args and **kwargs.

# 1. *args (Non-Keyword Arguments)
# The asterisk (*) allows the function to accept any number of positional arguments.
# Python packs them into a Tuple behind the scenes.
def add_all_numbers(*args):
    # args is just a tuple: e.g., (10, 20, 30)
    total = 0
    for num in args:
        total += num
    return total

print("Sum of 3 numbers:", add_all_numbers(10, 20, 30))
print("Sum of 5 numbers:", add_all_numbers(1, 2, 3, 4, 5))

# 2. **kwargs (Keyword Arguments)
# The double asterisk (**) allows the function to accept any number of keyword arguments.
# Python packs them into a Dictionary behind the scenes.
def build_profile(first_name, last_name, **kwargs):
    # kwargs is a dictionary containing the extra key-value pairs
    profile = {"first": first_name, "last": last_name}
    
    # Iterate through the dictionary and add items to the profile
    for key, value in kwargs.items():
        profile[key] = value
        
    return profile

# We can pass as many extra named arguments as we want
user = build_profile("Aryan", "HQ", location="Delhi", course="BCA", verified=True)
print(user)