from itertools import permutations
def per(string):
    words = [''.join(perm) for perm in permutations(string)]
    print(set(words))