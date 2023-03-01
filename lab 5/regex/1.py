import re

pattern = r'a{1}b*' #r - raw string
                    #a{1} means that the preceding 'a' should appear 1 time
                    #b* means that the preceding 'b' should appear zero or more times
                    #b+ means that the preceding 'b' should appear one or more times
                    #b? means that the preceding 'b' should appear zero or one times

string = ['ab', 'acb', 'abb', 'abbb', 'acbb', 'a', 'abc', 'aaab']

for s in string:
    if re.search(pattern, s):
        print(f"'{s}' matches the pattern")
    else:
        print(f"'{s}' does not match the pattern")
