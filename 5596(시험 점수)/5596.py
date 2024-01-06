import sys

S = list(map(int, sys.stdin.readline().split()))
T = list(map(int, sys.stdin.readline().split()))
listA = [sum(S), sum(T)]
listA.sort()

print(listA[-1])
