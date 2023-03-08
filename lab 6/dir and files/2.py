import os

path = r"C:\Users\kulek\Documents\GitHub\test\lab 6"

if not os.path.exists(path): #existence
    print("The specified path does not exist.")
else:
    print("The specified path exists.")

    if os.access(path, os.R_OK): #readability
        print("The specified path is readable.")
    else:
        print("The specified path is not readable.")

    if os.access(path, os.W_OK): #writability
        print("The specified path is writable.")
    else:
        print("The specified path is not writable.")

    if os.access(path, os.X_OK): #executability (run the file)
        print("The specified path is executable.")
    else:
        print("The specified path is not executable.")