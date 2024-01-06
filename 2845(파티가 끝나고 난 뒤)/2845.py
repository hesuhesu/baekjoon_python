import sys

L,P = map(int, sys.stdin.readline().split())
n = L*P
a1,a2,a3,a4,a5 = map(int, sys.stdin.readline().split())

print((a1-n),(a2-n),(a3-n),(a4-n),(a5-n))
