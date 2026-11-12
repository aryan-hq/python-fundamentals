# SAVING DICTIONARIES AND LISTS (The JSON Module)

# In Python, we have Lists and Dictionaries. But you CANNOT write a dictionary 
# directly to a text file. (file.write({"name": "Aryan"}) will crash).

# THE FIX: JSON (JavaScript Object Notation)
# JSON is the universal format for saving and sending data on the internet. 
# Python has a built-in module that flawlessly converts Dictionaries <--> JSON Text Files.

import json

# Here is a complex dictionary 
user_profile = {
    "first_name": "Aryan",
    "last_name": "HQ",
    "age": 20,
    "course": "B. Tech",
    "skills": ["C", "Python", "HTML"],
    "verified": True
}

# 1. Saving (Dumping) the Dictionary to a file
# We use json.dump(data_to_save, file_object, indent)
with open("profile.json", "w") as json_file:
    # indent=4 makes the file beautifully formatted and easy for humans to read
    json.dump(user_profile, json_file, indent=4)
    print("Profile successfully saved to profile.json!")

# 2. Loading the Dictionary back from the file
# We use json.load(file_object)
with open("profile.json", "r") as json_file:
    loaded_profile = json.load(json_file)
    
print("\n--- Loaded Profile ---")
# Python automatically converts the JSON file back into a perfect Python dictionary!
print(type(loaded_profile))
print(f"Name: {loaded_profile['first_name']}, Skills: {loaded_profile['skills']}")