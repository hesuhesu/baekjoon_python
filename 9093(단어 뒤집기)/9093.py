import sys

T = int(sys.stdin.readline())

for i in range(T) :
    listA = list(map(str, sys.stdin.readline().strip().split()))
    listB = []
    for j in listA :
        listB.append(j[::-1])
    
    for k in listB :
        print(k, end = ' ')
    print()
