import sys

T = int(sys.stdin.readline())
for i in range(T) :
    a, b, c = map(int, input().split())
    print(min(a, min(b, c)))
