import sys

listA = [[0 for x in range(100) ] for y in range(100)]

N,M = list(map(int, sys.stdin.readline().split()))

for i in range(N) :
    x1, y1, x2, y2 = list(map(int, sys.stdin.readline().split()))

    for j in range(x1,x2+1) :
        for k in range(y1, y2+1) :
            listA[j-1][k-1] += 1

result = 0
for i in range(100) :
    for j in range(100) :
        if listA[i][j] > M :
            result += 1
print(result)
