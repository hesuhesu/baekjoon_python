num = int(input())
listA = list(map(int, input().split()))
result = 0

for i in listA :
    number = 0
    if (i == 1) :
        continue
    for j in range(2,i) :
        if(i%j == 0) :
            number += 1
    if (number == 0) :
        result += 1
        
print(result)
