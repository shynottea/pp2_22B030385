filename = r"C:\Users\kulek\Documents\GitHub\test\lab 6\dir and files\4.py"

with open(filename, "r") as file:
    num_lines = 0
    for line in file:
        num_lines += 1

print(f"The file '{filename}' has {num_lines} lines.")