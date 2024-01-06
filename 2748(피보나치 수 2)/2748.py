import sys

n = int(sys.stdin.readline())

listA = [1,1]

for i in range(2,n+1) :
    listA.append(listA[-1] + listA[-2])

print(listA[n-1])
