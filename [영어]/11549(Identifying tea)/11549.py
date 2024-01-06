import sys

T = int(sys.stdin.readline())
result = 0
listA = list(map(int, sys.stdin.readline().split()))

for i in listA :
    if i == T :
        result += 1

print(result)
