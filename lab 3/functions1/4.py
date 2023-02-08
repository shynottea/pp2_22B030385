def filter_prime(nums):
    a = [int(x) for x in nums.split()]
    return list(filter(lambda x: all(x % i != 0 for i in range(2, int(x ** 0.5) + 1)) and x != 1, a))