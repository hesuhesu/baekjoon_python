import sys

N = int(sys.stdin.readline())
listA = list(map(int, sys.stdin.readline().split()))

for i in range(1,N) :
    listA[i] = max(listA[i], listA[i-1] + listA[i])

print(max(listA))
