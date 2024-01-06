import sys

n = int(sys.stdin.readline())

for _ in range(n):
    d, f, p = map(float, sys.stdin.readline().split())
    print("${:.2f}".format(round(d * f * p, 2)))
