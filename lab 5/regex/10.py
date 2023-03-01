import re

pattern = r'([a-z])([A-Z])'

s1 = "myCamelCaseString"

s2= re.sub(pattern, r'\1_\2', s1).lower() #\1 refers to the contents of the first captured group
                                         #\2 refers to the contents of the second captured group
                                         #lower() is a string method that converts all the alphabetic characters in a string to lowercase

print(s2)