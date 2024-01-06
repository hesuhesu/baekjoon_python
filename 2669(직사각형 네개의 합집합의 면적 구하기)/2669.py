import sys

dp = [[0 for _ in range(101)] for _ in range(101)]
result = 0

for i in range(4) :
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    for j in range(x1, x2):
        for k in range(y1, y2):
            if dp[j][k] == 0 :
                dp[j][k] = 1
                result += 1
print(result)
