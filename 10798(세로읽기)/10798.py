import sys

dp = []
result = ""
max_len = 0
for i in range(5):
    stringA = list(sys.stdin.readline().rstrip())
    dp.append(stringA)

    if len(stringA) > max_len :
        max_len = len(stringA)

for i in range(max_len):
    for j in range(5) :
        if i < len(dp[j]):
            result += dp[j][i]

print(result)