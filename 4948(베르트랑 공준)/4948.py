import sys
import math

listA = []
for i in range(2,246913):
    if i == 1 :
        continue
    for j in range(2,int(math.sqrt(i)+1)) :
        if i % j == 0 :
            break
    else :
        listA.append(i)

while 1 :
    num = int(sys.stdin.readline())
    result = 0
    if num == 0 :
        break
    
    for i in listA:
        if num < i <= 2*num:
            result += 1
    print(result)
