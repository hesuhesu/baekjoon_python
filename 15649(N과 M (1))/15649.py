import sys
from itertools import permutations

N,M= map(int, sys.stdin.readline().split())

listA = list(range(1,N+1))
combi = list(permutations(listA,M))

for i in combi :
    for j in i :
        print(j, end = ' ')
    print('')
