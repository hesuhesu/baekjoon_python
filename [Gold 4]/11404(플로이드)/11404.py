import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

DP = [[sys.maxsize] * (n+1) for _ in range(n+1)]

for i in range(1,n+1):
    DP[i][i] = 0
for i in range(m):
    a,b,c = map(int, sys.stdin.readline().split())
    DP[a][b] = min(c, DP[a][b])

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            DP[i][j] = min(DP[i][k] + DP[k][j], DP[i][j])

for i in range(1, n+1) :
    for j in range(1, n+1) :
        if DP[i][j] == sys.maxsize:
            print(0, end = " ")
        else :
            print(DP[i][j], end = " ")
    print("")
