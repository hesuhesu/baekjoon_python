import sys

num = int(input())

result = 0
for i in range(num) :
    listA = list(sys.stdin.readline())
    listB = []
    check = 0
    for j in range(len(listA)) :
        if listA[j] == listA[j-1] :
            pass
        elif listA[j] != listA[j-1] :
            if listA[j] in listB :
                check += 1
                break
            else :
                listB.append(listA[j])
    if check == 0 :
        result += 1
print(result)
