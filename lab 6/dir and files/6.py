import os
import string

directory = r"C:\python\for lab 6"

for letter in string.ascii_uppercase: #The string.ascii_uppercase constant is a string containing all the uppercase ASCII letters, from A to Z.
    filename = letter + ".txt"
    filepath = os.path.join(directory, filename)
    with open(filepath, "w") as file:
        file.write("This is file " + letter)