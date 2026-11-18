# ENCAPSULATION AND PROPERTY DECORATORS

# Encapsulation is the bundling of data and restricting direct access to it 
# to prevent accidental modification. 

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner          # Public attribute (accessible anywhere)
        self._bank_branch = "Main"  # Protected (Convention: "Please don't touch this from outside")
        self.__balance = balance    # Private (Strictly hidden from the outside using double underscore)

    # 1. Name Mangling (How Python hides private variables)
    # Python changes self.__balance to self._BankAccount__balance internally 
    # to prevent you from easily accessing it outside the class.

    # 2. Getters and Setters (The Modern Pythonic Way)
    # Instead of writing get_balance() and set_balance() methods, Python uses the @property decorator.
    
    @property # This acts as the "Getter"
    def balance(self):
        return self.__balance

    @balance.setter # This acts as the "Setter"
    def balance(self, amount):
        if amount < 0:
            print("Error: Balance cannot be negative.")
        else:
            self.__balance = amount

account = BankAccount("Aryan", 5000)

# Accessing Public and Protected (Protected is just an honor system in Python)
print(account.owner)
print(account._bank_branch)

# print(account.__balance) # THIS WILL CRASH! (AttributeError)

# Using the @property getter (Notice we don't use parentheses like a method call!)
print(f"Current Balance: {account.balance}")

# Using the @property setter
account.balance = 10000    # Works perfectly
account.balance = -500     # Triggers our error check!
print(f"New Balance: {account.balance}")