import sys

N = int(sys.stdin.readline())

listA = list(map(int, sys.stdin.readline().split()))
listB = list(listA)
listA.sort()

dicA = {}
dicNum = 0
for i in range(len(listA)) :
    if listA[i] not in dicA :
        dicA[listA[i]] = dicNum
        dicNum += 1
    
for i in listB :
    print(dicA[i], end= ' ')
