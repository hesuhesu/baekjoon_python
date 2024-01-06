import sys

N = int(sys.stdin.readline())
listA = list(map(int, sys.stdin.readline().split()))
dp1, dp2 = [1]*N, [1]*N
for i in range(1, N):
    if listA[i] <= listA[i-1]:
        dp1[i] = max(dp1[i], dp1[i-1]+1)
    if listA[i] >= listA[i-1]:
        dp2[i] = max(dp2[i], dp2[i-1]+1)
print(max(max(dp1), max(dp2)))
