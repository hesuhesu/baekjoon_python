import sys

while 1 :

    listA = list(map(int, str(sys.stdin.readline().strip())))
    if listA[0] == 0 :
        break

    result = 0
    for i in range(len(listA)//2) :
        if listA[i] == listA[len(listA)-1-i] :
            pass
        elif listA[i] != listA[len(listA)-1-i] :
            print("no")
            result += 1
            break

    if result == 0 :
        print("yes")
