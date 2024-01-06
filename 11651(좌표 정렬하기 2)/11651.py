import sys

num = int(sys.stdin.readline())

listA = []
for i in range(num) :
    listA.append(list(map(int, sys.stdin.readline().split())))

listA.sort(key = lambda  x : (x[1], x[0]))

for i,j in listA :
    print(i,j)
