# 1. THE TRADITIONAL WAY (open and close)

# Python uses the built-in open() function to handle files. It returns a file object.

# Writing to a file (Mode: "w")
# The "w" mode will OVERWRITE the file if it exists, or CREATE it if it doesn't.
file = open("student_data.txt", "w")
file.write("Name: Aryan\n")
file.write("Course: BCA\n")

# You MUST close the file to save the data from RAM to the hard drive 
# and free up system resources.
file.close() 

# Appending to a file (Mode: "a")
# The "a" mode adds data to the END of the file without erasing what's already there.
file = open("student_data.txt", "a")
file.write("Location: Delhi\n")
file.close()

# There is are few more modes : 
# 'x' : create a new file and open it for writing.
# 'b' : binary mode.
# 't' : text mode (default)
# '+' : open a disk file for updating (reading and writing)

# Reading from a file (Mode: "r")
# The "r" mode is the default. If the file doesn't exist, it crashes with a FileNotFoundError.
file = open("student_data.txt", "r")
content = file.read() # Reads the entire file into one massive string
print("--- File Contents ---")
print(content)
file.close()


# 2. File io using 'with' statement

# PROBLEM WITH THE TRADITIONAL WAY:
# If your program crashes while writing to a file, the file.close() line 
# never runs. The file can get corrupted, and memory is leaked.

# THE SOLUTION: The 'with' statement.
# The 'with' statement creates a safe "context block". As soon as the block ends
# (or even if the program crashes inside it), Python AUTOMATICALLY closes the file.
# You will almost NEVER see a professional Python developer use file.close().

print("\nWriting using 'with'...")

# Syntax: with open(filename, mode) as variable_name:
with open("secure_data.txt", "w") as file:
    file.write("This is highly secure data.\n")
    file.write("If the program crashes now, Python still closes the file safely!\n")
    # No file.close() needed here!


# 3. ADVANCED READING AND WRITING METHODS

# Let's create a quick file to read from
with open("lines.txt", "w") as f:
    f.write("Line 1: Apple\nLine 2: Banana\nLine 3: Cherry\n")

# A. Reading Line by Line (Memory Efficient)
# Using file.read() on a massive file will crash your RAM. 
# Instead, files are "iterable". You can loop through them just like a List.
print("\nReading line-by-line:")
with open("lines.txt", "r") as file:
    for line in file:
        # We use end="" because the file already has \n at the end of each line, 
        # and print() adds its own \n. This prevents double-spacing.
        print(line, end="") 

# B. readlines() Returns a LIST of strings
# Useful if you want to store the file in a list and access specific lines via index.
with open("lines.txt", "r") as f:
    lines_list = f.readlines()
    print("\n\nUsing readlines():")
    print(lines_list)          # Output: ['Line 1: Apple\n', 'Line 2: Banana\n', ...]
    print(lines_list[1])       # Accessing the second line directly

# C. readline() Reads strictly ONE line at a time
with open("lines.txt", "r") as f:
    print("\nUsing readline():")
    first = f.readline()
    second = f.readline()
    print("First call:", first, end="")
    print("Second call:", second, end="")

# D. writelines() Writes a LIST of strings into a file
# Note: It does NOT automatically add \n. You must include them in your list strings.
new_data = ["One\n", "Two\n", "Three\n"]
with open("numbers.txt", "w") as f:
    f.writelines(new_data)


# To delete a file from system
# step 1 : use "import os" to import built-in os module
# step 2 : use syntax : "os.remove("filename.txt")"