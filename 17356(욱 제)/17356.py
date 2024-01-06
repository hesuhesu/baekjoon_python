import sys

A, B = map(int, sys.stdin.readline().split())
M = (B-A)/400
print(1/(1+10**M))
