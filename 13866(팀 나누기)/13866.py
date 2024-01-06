import sys

listA = list(map(int, sys.stdin.readline().split()))
intA = min(listA) + max(listA)

print(abs(sum(listA) - 2*intA))
