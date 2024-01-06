num_low = int(input())
num_high = int(input())

resultList = []
for i in (range(num_low, num_high+1)) :
    number = 0
    if (i > 1) :
        for j in range(2,i) :
            if(i%j == 0) :
                number += 1
                break # 계속 돌려도 되지만, 시간복잡도 단축을 위함.
        if (number == 0) :
            resultList.append(i)

if len(resultList) > 0 :
    print(sum(resultList))
    print(resultList[0])
else :
    print(-1)
