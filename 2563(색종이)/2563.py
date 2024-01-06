import sys

num = int(sys.stdin.readline())

listA = [[0 for _ in range(101)] for _ in range(101)]

for i in range(num) :
    x, y = map(int, sys.stdin.readline().split())
    for j in range(x, x+10) :
        for k in range(y, y+10) :
            listA[j][k] = 1

result = 0
for i in listA :
    result += i.count(1)
print(result)
