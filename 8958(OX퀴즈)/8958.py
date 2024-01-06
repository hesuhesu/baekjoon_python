num = int(input())

resultList = []
for i in range(num) :
    listA = []
    checklist = list(input())
    sum = 0
    num = 0
    for i in checklist :
        
        if i == "O" :
            num += 1
            listA.append(num)
        else :
            num = 0
            listA.append(num)

    for i in listA :
        sum += i
    
    resultList.append(sum)

for i in resultList :
    print(i)
