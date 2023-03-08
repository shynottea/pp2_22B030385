filename = r"C:\python\for lab 6\5.txt"
mylist = ["apple", "banana", "cherry", "date"]

with open(filename, "w") as file:
    for item in mylist:
        file.write(item + "\n")