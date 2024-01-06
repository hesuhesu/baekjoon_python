import sys

N,A,B = map(int, sys.stdin.readline().split())

if A == B :
    print("Anything")
elif A < B :
    print("Bus")
else :
    print("Subway")
