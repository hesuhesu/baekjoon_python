import sys

N,M = map(int,sys.stdin.readline().split())

listA = []
for i in range(N):
    listA.append(i+1)

for i in range(M):
    i,j = map(int, sys.stdin.readline().split())
    listB = listA[i-1:j]
    listB.reverse()
    listA[i-1:j] = listB

for i in listA :
    print(i, end = " ")