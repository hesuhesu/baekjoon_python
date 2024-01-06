import sys

A, B = map(int, sys.stdin.readline().split())
listA = []

for i in range(1,B+1) :
    for j in range(i) :
        listA.append(i)

print(sum(listA[A-1:B]))
