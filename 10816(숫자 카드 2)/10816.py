import sys

N = int(sys.stdin.readline())
listA = list(map(int, sys.stdin.readline().split()))

dicA = {}
for i in listA :
    if i in dicA :
        dicA[i] += 1
    else:
        dicA[i] = 1

M = int(sys.stdin.readline())
listB = list(map(int, sys.stdin.readline().split()))

for i in listB :
    if i not in dicA :
        print(0, end = " ")
    else :
        print(dicA[i], end = " ")
