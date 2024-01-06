import sys

while 1 :
    listA = list(map(int, sys.stdin.readline().split()))
    listA.sort()
    if listA[-1] == 0 :
        break

    if (listA[-1])**2 == (listA[0])**2 + (listA[1])**2 :
        print("right")
    else :
        print("wrong")
