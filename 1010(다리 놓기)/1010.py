import sys

num = int(sys.stdin.readline())

for i in range(num) :
    result = 1
    N,M = map(int, sys.stdin.readline().split())
    for j in range(N) :
        result *= M
        M -= 1
    for k in range(1,N+1) :
        result = result // k
    print(result)
