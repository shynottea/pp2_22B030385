def prime(a):
    return list(filter(lambda x: all(x % i != 0 for i in range(2, int(x ** 0.5) + 1)) and x != 1, a))

list1 = input().split()
nums = list(map(int, list1))
print(prime(nums))