import sys

K, N, M = map(int, sys.stdin.readline().split())

if (M > K * N):
    print(0)
else :
    print(K*N - M)
