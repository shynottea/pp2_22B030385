import re
pattern = r'([a-z])([A-Z])'

s1 = "TheQuickBrownFoxJumpsOverTheLazyDog"

s2 = re.sub(pattern, r'\1 \2', s1)

print(s2)