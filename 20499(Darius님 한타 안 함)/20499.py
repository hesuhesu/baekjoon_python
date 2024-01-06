import sys

K,D,A = map(int, sys.stdin.readline().split("/"))

if (K + A < D) | (D == 0) :
    print("hasu")
else :
    print("gosu")
