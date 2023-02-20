def div_by_3_and_4_gen(n):
    for i in range(0, n+1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

n = int(input("Enter a value for n: "))
div_numbers = div_by_3_and_4_gen(n)
print(','.join(map(str, div_numbers))) 