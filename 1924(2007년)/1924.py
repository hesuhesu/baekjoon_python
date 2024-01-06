import sys

x,y = map(int, sys.stdin.readline().split())

listA = [31,28,31,30,31,30,31,31,30,31,30,31]
listB = ['SUN','MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
result = y
for i in range(x-1) :
    result += listA[i]

print(listB[(result % 7)])
