import sys, math

L = int(sys.stdin.readline())
A = int(sys.stdin.readline())
B = int(sys.stdin.readline())
C = int(sys.stdin.readline())
D = int(sys.stdin.readline())

if math.ceil(A/C) > math.ceil(B/D) :
    print(L - math.ceil(A/C))
else :
    print(L - math.ceil(B/D))
