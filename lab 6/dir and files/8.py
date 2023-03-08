import os

file_path = r"C:\python\for lab 6\8.txt"

if os.access(file_path):
    if os.access(file_path, os.W_OK):
        os.remove(file_path)
        print(f"{file_path} deleted successfully")
    else:
        print(f"{file_path} cannot be deleted. No write access.")
else:
    print(f"{file_path} not found.")