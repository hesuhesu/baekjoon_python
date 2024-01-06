import sys

a,b = map(int, sys.stdin.readline().split())

if a - a*(b/100) >= 100 :
    print(0)
else :
    print(1)
