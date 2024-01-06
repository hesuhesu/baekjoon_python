import sys

N = int(sys.stdin.readline())

listA = []
for i in range(N) :
    listA.append(list(map(int, sys.stdin.readline().split())))

Rank = []
for i in range(N):
    count = 1
    for j in range(N):
        if (listA[i][0] < listA[j][0]) & (listA[i][1] < listA[j][1]) :
            count += 1 
    Rank.append(count)
 
for i in Rank:
    print(i, end=' ')
