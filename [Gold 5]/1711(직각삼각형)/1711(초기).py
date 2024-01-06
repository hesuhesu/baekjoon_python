import sys
from itertools import combinations

N = int(sys.stdin.readline())

listA = []
for i in range(N) :
    listA.append(list(map(int, sys.stdin.readline().split())))

result = 0
combi = list(combinations(listA, 3))

for i in combi :
    listB = []
    listB.append(abs(i[0][0]-i[1][0])**2 + abs(i[0][1]-i[1][1])**2)
    listB.append(abs(i[0][0]-i[2][0])**2 + abs(i[0][1]-i[2][1])**2)
    listB.append(abs(i[1][0]-i[2][0])**2 + abs(i[1][1]-i[2][1])**2)
    listB.sort()
    if listB[-1] == listB[0] + listB[1] :
        result += 1

print(result)
