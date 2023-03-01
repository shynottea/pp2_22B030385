import re

pattern = r'a{1}b{2,3}'
                        #b{2,3} means that the preceding 'b' should appear 2 or 3 times

string = ['ab', 'acb', 'abb', 'abbb', 'acbb', 'a', 'abc', 'aaab']

for s in string:
    if re.match(pattern, s):
        print(f"'{s}' matches the pattern")
    else:
        print(f"'{s}' does not match the pattern")