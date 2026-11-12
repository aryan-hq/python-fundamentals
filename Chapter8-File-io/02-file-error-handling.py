# SAFELY HANDLING MISSING FILES

# What happens if you try to read a file that doesn't exist?
# Python panics and throws a FileNotFoundError, crashing your entire program.

# We use a try-except block to gracefully catch the error and keep the program running.

try:
    with open("this_file_does_not_exist.txt", "r") as f:
        content = f.read()
        
except FileNotFoundError:
    print("Error: The file you are looking for does not exist!")
    # Here you could create the file, or ask the user for a new filename.
    
except PermissionError:
    print("Error: You do not have admin rights to open this file!")
    
finally:
    # The 'finally' block ALWAYS runs, whether the code crashed or succeeded.
    print("File reading attempt finished.")