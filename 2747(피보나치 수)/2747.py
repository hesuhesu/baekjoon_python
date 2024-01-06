import sys

n = int(sys.stdin.readline())

listA = [1,1]
for i in range(2,n) : 
    listA.append(listA[i-1]+listA[i-2])

print(listA[-1])
