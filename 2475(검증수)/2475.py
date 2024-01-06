import sys

listA = list(map(int, sys.stdin.readline().split()))

result = 0
for i in listA :
    result += i**2

print(result % 10)
