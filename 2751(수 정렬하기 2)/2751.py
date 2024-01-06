import sys

num = int(sys.stdin.readline())

listA = []
for i in range(num) :
    listA.append(int(sys.stdin.readline()))

for j in sorted(listA) :
    print(j)
