import re

s1 = "Hello, world. How are you today?"

s2 = re.sub(r'[ ,.]+', ':', s1)

print(s2)