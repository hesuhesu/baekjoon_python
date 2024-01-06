a,b = map(int, input().split())

listA = []
for i in range(a) :
    listA.append(list(map(int, input().split())))

listB = []
for i in range(a) :
    listB.append(list(map(int, input().split())))

finalList = []
for i in range(a) :
    TestList = []
    for j in range(b) :
        TestList.append(listA[i][j] + listB[i][j])
    print(*TestList)
