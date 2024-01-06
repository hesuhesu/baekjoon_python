import sys

N = int(sys.stdin.readline())
result = 0
listA = list(map(int, sys.stdin.readline().split()))

for i in listA :
    if i >= N :
        result += N
    else :
        result += i

print(result)
