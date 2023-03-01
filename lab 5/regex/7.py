'''
Snake case strings are text strings that use underscores (_) between words.
For example, "hello_world" is a snake case string.
'''

'''
Camel case strings are text strings that start with a lowercase letter and use uppercase letters to denote the start of each subsequent word.
For example, "hello World" is a camelcase string.
'''

import re

pattern = r'_([a-z])'

s1 = "my_snake_case_string"

s2 = re.sub(pattern, r'\1'.upper(), s1.title().replace('_', ''))

print(s2)