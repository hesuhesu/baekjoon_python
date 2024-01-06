import sys

num = list(map(int, sys.stdin.readline().strip()))

num.sort()
result = 0
for i in range(len(num)) :
    result += num[i] * (10**i)
print(result)
