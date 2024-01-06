import sys

num = int(sys.stdin.readline())
listA = []
for i in range(1,num+1) :
    intA = list(map(int, str(i)))
    if (sum(intA)+i) == num :
        print(i)
        break
    if i == num :
        print(0)
