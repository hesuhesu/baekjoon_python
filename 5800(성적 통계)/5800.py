import sys

N = int(sys.stdin.readline())

for i in range(N) :
    listA = list(map(int, sys.stdin.readline().split()))
    del listA[0]
    listA.sort()
    result = 0
    for j in range(len(listA)-1) :
        if listA[j+1] - listA[j]  > result :
            result =  listA[j+1] - listA[j]
    print("Class {}".format(i+1))
    print("Max {}, Min {}, Largest gap {}".format(max(listA),min(listA),result))
