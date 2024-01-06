from itertools import combinations
import sys

num, sum1 = map(int, sys.stdin.readline().split())
listA = list(map(int, sys.stdin.readline().split()))
listB = []
for i in list(combinations(listA, 3)) :
    if sum(i) <= sum1 :
        listB.append(sum(i))
    
listB.sort()
print(listB[-1])
