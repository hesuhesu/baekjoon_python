import sys

A = int(sys.stdin.readline())
B = int(sys.stdin.readline())
C = int(sys.stdin.readline())
D = int(sys.stdin.readline())
E = int(sys.stdin.readline())
if (A < 0):
    print(C*(-A) + D + E*B)
elif (A > 0) :
    print((B-A)*E)
