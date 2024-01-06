import sys

M = int(sys.stdin.readline())

result = 1
for i in range(M) :
    X,Y = map(int, sys.stdin.readline().split())
    if X == result :
        result = Y
    elif Y == result :
        result = X

print(result)
