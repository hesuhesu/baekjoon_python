import sys

N, M = map(int, sys.stdin.readline().split())

listA = [0]*N
for _ in range(M) :
    i, j, k = map(int, sys.stdin.readline().split())
    for __ in range(i-1,j) :
        listA[__] = k

for _ in listA :
    print(_, end = ' ')
