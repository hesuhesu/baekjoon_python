import sys

N, M = map(int, sys.stdin.readline().split())

count = 0
listA = []
for i in range(N):
    listA.append(sys.stdin.readline())

setA = set(listA)
for i in range(M):
    stringA = sys.stdin.readline()
    if stringA in setA :
        count += 1

print(count)
