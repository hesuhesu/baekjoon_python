import sys

listA = []
for i in range(4) :
    listA.append(int(sys.stdin.readline()))

listB = []
for i in range(2) :
    listB.append(int(sys.stdin.readline()))

listA.sort()
listB.sort()

print(sum(listA[1:]) + sum(listB[1:]))
