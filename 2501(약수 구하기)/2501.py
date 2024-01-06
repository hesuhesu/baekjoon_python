import sys

N, K = map(int, sys.stdin.readline().split())

listA = []
for i in range(1,N+1) :
    if N % i == 0 :
        listA.append(i)

if len(listA) >= K :
    print(listA[K-1])
else :
    print(0)
