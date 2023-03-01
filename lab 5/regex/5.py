import re

pattern = r'a.+b$' #. - any character

string = "The quick brown fox jumps over a lazy dog b"

match = re.search(pattern, string)

if match:
    print("Match found:", match.group())
else:
    print("No match found.")