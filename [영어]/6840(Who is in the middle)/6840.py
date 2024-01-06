import sys

listA = []
for _ in range(3) :
    listA.append(int(sys.stdin.readline()))
listA.sort()
print(listA[1])
