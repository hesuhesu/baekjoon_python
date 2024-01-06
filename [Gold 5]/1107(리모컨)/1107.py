import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
listA = list(map(str, sys.stdin.readline().split()))
result = abs(N - 100)

for i in range(1000001):
    for j in str(i):
        if j in listA:
            break
    else:
        result = min(result, len(str(i)) + abs(i - N))

print(result)