import sys

def floyd_warshall(listA):
    for i in range(len(listA)):
        for j in range(len(listA)):
            for k in range(len(listA)):
                if listA[j][i] and listA[i][k]:
                    listA[j][k] = 1

N = int(sys.stdin.readline())
listA = []
for i in range(N):
    listA.append(list(map(int, sys.stdin.readline().split())))

floyd_warshall(listA)

for i in listA :
    print(*i)