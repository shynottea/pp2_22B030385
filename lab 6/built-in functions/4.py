import time

num = int(input())
latency = int(input())

time.sleep(latency / 1000) #milli - 10^-3

result = num ** (1/2)

print(f"Square root of {num} after {latency} milliseconds is {result}")