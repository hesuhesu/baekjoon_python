import sys

listA = []

for i in range(3) :
    listA.append(int(sys.stdin.readline()))

listB = []
for i in range(2) :
    listB.append(int(sys.stdin.readline()))

print(min(listA) + min(listB) - 50)
