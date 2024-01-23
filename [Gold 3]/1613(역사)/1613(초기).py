import sys

n,k = map(int, sys.stdin.readline().split())

dp = []
for i in range(n):
    dp.append([0] * n)

for i in range(k):
    event1, event2 = map(int, sys.stdin.readline().split())
    dp[event1 - 1][event2 - 1] = 1

for k in range(n):
    for i in range(n):
        for j in range(n):
            if dp[i][k] and dp[k][j]:
                dp[i][j] = 1

s = int(sys.stdin.readline())
for i in range(s):
    s1, s2 = map(int, sys.stdin.readline().split())
    if dp[s1-1][s2-1] == 1:
        print(-1)
    elif dp[s2-1][s1-1] == 1:
        print(1)
    else:
        print(0)