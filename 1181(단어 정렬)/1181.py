import sys

num = int(sys.stdin.readline())

listA = []
for i in range(num) :
    listA.append(sys.stdin.readline().strip())

listB = set(listA)
listA = list(listB)
listA.sort()
listA.sort(key=len)

for i in listA :
    print(i)
