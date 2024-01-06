All_list = list(range(1,31))
listA = []
for i in range(28) :
    listA.append(int(input()))

for i in All_list :
    if i not in listA :
        print(i)
