import sys

while 1 :
    listA = sorted(list(map(int, sys.stdin.readline().split())))
    if listA[2] == 0 :
        break
    
    if listA[2] >= listA[0] + listA[1] :
        print("Invalid")
    else :
        listA = set(listA)
        if len(listA) == 1 :
            print("Equilateral")
        elif len(listA) == 2 :
            print("Isosceles")
        else :
            print("Scalene")