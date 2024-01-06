import sys

A,B,C = map(int, sys.stdin.readline().split())
print(A * max(B, C) // min(B, C))
