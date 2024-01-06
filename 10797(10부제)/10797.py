import sys

N = int(sys.stdin.readline())
listA = list(map(int, sys.stdin.readline().split()))

result = 0
for i in listA :
    if (i % 10 == N):
        result+=1

print(result)
