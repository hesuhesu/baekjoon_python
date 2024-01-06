listA = [1,1,1,2,2]

for i in range(96) :
    listA.append(listA[i] + listA[i+4])

num = int(input())

listB = []
for i in range(num) :
    num2 = int(input())
    listB.append(num2)

for i in range(len(listB)) :
    print(listA[listB[i]-1])
