import re

pattern = r'[A-Z]{1}[a-z]*'

s = 'HelloWorldHowAreYou'

result = re.findall(pattern, s)

print(result)