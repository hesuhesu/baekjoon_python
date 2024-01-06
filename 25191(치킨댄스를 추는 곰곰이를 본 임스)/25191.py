import sys

N = int(sys.stdin.readline())
A,B = map(int, sys.stdin.readline().split())

if (A//2 + B > N) :
    print(N)
else :
    print(A//2 + B)
