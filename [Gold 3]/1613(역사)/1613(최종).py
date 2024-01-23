import sys
input = sys.stdin.readline

def floydWarshall():
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if dp[i][k] and dp[k][j]:
                    dp[i][j] = 1


N, K = map(int, input().split())
dp = [[0] * N for _ in range(N)]

for _ in range(K):
    a, b = map(int, input().split())
    dp[a - 1][b - 1] = 1

floydWarshall()

s = int(input())
for _ in range(s):
    a, b = map(int, input().split())
    if dp[a - 1][b - 1] == 1:
        print(-1)
    elif dp[b - 1][a - 1] == 1:
        print(1)
    else:
        print(0)