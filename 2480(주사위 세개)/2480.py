listA = list(map(int, input().split()))

final_num = 0
for i in range(1,7) :
    num = listA.count(i) # 해당 숫자가 몇 개인지 알려줌.

    if num == 2 :
        final_num = 1000+(i*100)
        break
    elif num == 3 :
        final_num = 10000 + (i*1000)
        break
    elif num == 1 :
        final_num = i * 100
    
print(final_num)
