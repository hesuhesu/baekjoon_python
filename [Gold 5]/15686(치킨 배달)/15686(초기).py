import sys

num1, num2 = map(int, sys.stdin.readline().split())
doubleList = []
checkList_1 = []
checkList_2 = []
for i in range(num1) :
    doubleList.append(list(map(int, sys.stdin.readline().split())))
    for j in range(num1) :
        if doubleList[i][j] == 2 :
            checkList_2.append([i,j])
        elif doubleList[i][j] == 1 :
            checkList_1.append([i,j])

resultList = []

if num2 == 1 :
    for i in range(len(checkList_2)) :
        checkList_3 = []
        for j in range(len(checkList_1)) :
            List_x = abs(checkList_2[i][0] - checkList_1[j][0])
            List_y = abs(checkList_2[i][1] - checkList_1[j][1])
            checkList_3.append(List_x + List_y)
        resultList.append(sum(checkList_3))

    resultList.sort()
    print(sum(resultList[:num2]))


elif num2 > 1 :
    checkList_3 = []
    for i in range(len(checkList_1)) :
        
        for j in range(len(checkList_2)) :
            List_x = abs(checkList_2[j][0] - checkList_1[i][0])
            List_y = abs(checkList_2[j][1] - checkList_1[i][1])
            checkList_3.append(List_x + List_y)
        
    checkList_3.sort()
    print(sum(checkList_3[:len(checkList_1)]))
