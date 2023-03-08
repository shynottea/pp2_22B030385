string = "Abc Def Ghi Jkl Mno"

upper_count = sum(1 for c in string if c.isupper()) #"1 for ..." generates a value of 1 for each upper case character in the string
lower_count = sum(1 for c in string if c.islower())

print(f"Upper case letters: {upper_count}")
print(f"Lower case letters: {lower_count}")