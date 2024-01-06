import sys

li = list(map(int, sys.stdin.readline().split()))
x, y, r = map(int, sys.stdin.readline().split())
print(li.index(x)+1 if x in li else 0)
