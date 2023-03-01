import re

pattern = r'[A-Z]{1}[a-z]+'

string = "The quick Brown fox jumps over The Lazy Dog"

sequence = re.findall(pattern, string)

print(sequence)