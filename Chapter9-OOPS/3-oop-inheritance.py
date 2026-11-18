# INHERITANCE AND SUPER()

# Inheritance allows a new class (Child) to take on the attributes and methods 
# of an existing class (Parent), promoting code reuse (DRY principle).

# 1. Parent Class
class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def login(self):
        print(f"{self.username} has logged in.")

# 2. Child Class (Inherits from User)
# We put the Parent class name in parentheses when defining the Child class.
class Admin(User):
    def __init__(self, username, email, admin_level):
        # super() calls the Parent class's __init__ method so we don't 
        # have to rewrite the username and email assignment code.
        super().__init__(username, email)
        
        # Now we add the attribute specific to the Admin
        self.admin_level = admin_level

    # 3. Method Overriding
    # If we define a method with the SAME NAME as the parent, it overrides it.
    def login(self):
        print(f"ADMIN {self.username} (Level {self.admin_level}) has logged in securely.")

    def delete_user(self, user_to_delete):
        print(f"{self.username} deleted the user {user_to_delete}.")


standard_user = User("sam_99", "sam@gmail.com")
admin_user = Admin("aryan_hq", "aryan@admin.com", level=3)

# Both can login, but they trigger different methods (Method Overriding)
standard_user.login()
admin_user.login()

# Admin has access to methods the standard user does not
admin_user.delete_user("spammer_123")
# standard_user.delete_user("someone") # THIS WOULD CRASH!