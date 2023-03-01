import re

pattern = r'[a-z]+_[a-z]+' 

string = 'hello_world is a popular programming convention'

match = re.findall(pattern, string)

print(match)