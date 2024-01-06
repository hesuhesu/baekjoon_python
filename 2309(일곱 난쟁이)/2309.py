import sys

listA = []

hap = 0
for i in range(9) :
    num = int(sys.stdin.readline())
    hap += num
    listA.append(num)

for i in range(8) :
    check = 0
    for j in range(i+1,9) :
        if (hap - listA[i] - listA[j] == 100) :
            del listA[i]
            del listA[j-1]
            check += 1
            break
    
    if (check == 1) :
        listA.sort()
        for i in listA :
            print(i)
        break