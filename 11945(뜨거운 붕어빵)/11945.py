import sys

N, M = map(int, sys.stdin.readline().split())

listA = []
for i in range(N) :
    listA.append(sys.stdin.readline().strip()[::-1]) 

for i in listA :
    print(i)
