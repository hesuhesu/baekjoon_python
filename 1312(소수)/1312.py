import sys

A,B,N = map(int, sys.stdin.readline().split())

A %= B
for i in range(N-1):
    A = (A*10) % B
    
print((A * 10) // B)
