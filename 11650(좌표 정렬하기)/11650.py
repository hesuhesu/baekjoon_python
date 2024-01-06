import sys

num = int(sys.stdin.readline())

listA = []
for i in range(num) :
    listA.append(list(map(int, sys.stdin.readline().split())))

listA.sort()

for i,j in listA :
    print(i, j)
