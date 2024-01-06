import sys

n = list(map(int, sys.stdin.readline().strip()))

listA = [0 for i in range(10)]

for i in n :
    if (i == 9) | (i == 6) :
        if listA[6] == listA[9] :
            listA[6] += 1
        else :
            listA[9] += 1
    else :
        listA[i] += 1

print(max(listA))
