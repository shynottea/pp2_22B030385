import os

path = r"C:\Users\kulek\Documents\GitHub\test\lab 6\dir and files\3.py"

if not os.path.exists(path):
    print(f"The path '{path}' does not exist.")
else:
    print(f"The path '{path}' exists.")
    dirname = os.path.dirname(path)
    filename = os.path.basename(path)
    print(f"The directory portion of the path is '{dirname}'.")
    print(f"The filename portion of the path is '{filename}'.")