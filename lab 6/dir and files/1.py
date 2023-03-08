import os

path = r"C:\Users\kulek\Documents\GitHub\test\lab 6"

print("List of directories:")
for dirpath, dirnames, filenames in os.walk(path):
    for dirname in dirnames:
        print(os.path.join(dirpath, dirname))

print("List of files:")
for dirpath, dirnames, filenames in os.walk(path):
    for filename in filenames:
        print(os.path.join(dirpath, filename))

print("List of directories and files:")
for dirpath, dirnames, filenames in os.walk(path):
    for dirname in dirnames:
        print(os.path.join(dirpath, dirname))
    for filename in filenames:
        print(os.path.join(dirpath, filename))