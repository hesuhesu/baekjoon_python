import sys

N = int(sys.stdin.readline())
listA = list(map(int, sys.stdin.readline().split()))
checkList = [0]

for i in listA :
    checkList.append(checkList[-1] + i)

result = 0
for i in checkList :
    if i+50 in checkList :
        if i+50 == 100 :
            continue
        else :
            result += 1

print(result)
