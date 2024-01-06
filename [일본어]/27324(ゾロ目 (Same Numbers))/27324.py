import sys

N = int(sys.stdin.readline())

if (N % 10) == (N//10) :
    print(1)
else :
    print(0)
