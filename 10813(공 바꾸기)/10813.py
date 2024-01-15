import sys

N,M = map(int, sys.stdin.readline().split())
listA = []
for i in range(N):
    listA.append(i+1)
for _ in range(M) :
    i,j = map(int, sys.stdin.readline().split())
    listA[i-1], listA[j-1] = listA[j-1], listA[i-1]

for i in listA :
    print(i, end = " ")
