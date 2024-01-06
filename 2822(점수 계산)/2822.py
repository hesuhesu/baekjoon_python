import sys

listA = []
result = 0
for i in range(1,9) :
    append = int(sys.stdin.readline())
    listA.append([i,append])
    result += append

listA.sort(key = lambda x : x[1])
for i in range(3) :
    result -= listA[0][1]
    del listA[0]

listA.sort(key = lambda x : x[0])

print(result)
for i,j in listA :
    print(i, end = ' ')
