import sys

num = int(sys.stdin.readline())
listA = []
for i in range(num) :
    num2 = int(sys.stdin.readline())
    if num2 == 0 :
        listA.pop()
    else :
        listA.append(num2)

print(sum(listA))
