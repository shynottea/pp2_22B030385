source_file = r"C:\python\for lab 6\source.txt"
target_file = r"C:\python\for lab 6\target.txt"

with open(source_file, "r") as source:
    with open(target_file, "w") as target:
        target.write(source.read())