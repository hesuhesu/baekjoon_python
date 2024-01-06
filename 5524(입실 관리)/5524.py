import sys

N = int(sys.stdin.readline())

listA = []
for i in range(N) :
    listA.append((sys.stdin.readline().strip()).lower())

for i in listA :
    print(i)
