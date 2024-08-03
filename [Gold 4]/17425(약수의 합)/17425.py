import sys

MAX = 1000000
dp = [0] * (MAX + 1)
result = [0] * (MAX + 1)

for i in range(1, MAX + 1):
    j = 1
    while i * j <= MAX :
        dp[i*j] += i
        j += 1
    result[i] = result[i-1] + dp[i]

T = int(sys.stdin.readline())
for _ in range(T):
    print(str(result[int(sys.stdin.readline())]))
