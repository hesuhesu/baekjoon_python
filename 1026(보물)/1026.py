import sys

num = int(sys.stdin.readline())
listA = list(map(int, sys.stdin.readline().split()))
listB = list(map(int, sys.stdin.readline().split()))

listA = sorted(listA)
listB = sorted(listB, reverse=True)

result = 0
for i in range(num):
    result += listA[i]*listB[i]
print(result)
