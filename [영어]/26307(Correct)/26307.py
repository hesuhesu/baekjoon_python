import sys

HH, MM = map(int, sys.stdin.readline().split())

print(60*(HH-9) + MM)
