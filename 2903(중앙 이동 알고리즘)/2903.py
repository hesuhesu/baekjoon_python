import sys

N = int(sys.stdin.readline())
point = 2
for _ in range(1,N+1):
    point += (point - 1)

print(point ** 2)