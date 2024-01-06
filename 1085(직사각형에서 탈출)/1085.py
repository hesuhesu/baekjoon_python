import sys

listA = list(map(int, sys.stdin.readline().split()))

listA[2] = listA[2] - listA[0]
listA[3] = listA[3] - listA[1]
sorted(listA)

print(min(listA))
