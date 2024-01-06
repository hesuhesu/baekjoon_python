import sys

N = int(sys.stdin.readline())

for i in range(2*N//2) :
    print(" " * i, end='')
    print("*" * (2*N-1-2*i))

for i in range(2,N+1) :
    print(" " * (N-i), end='')
    print("*" * (2*i - 1))
