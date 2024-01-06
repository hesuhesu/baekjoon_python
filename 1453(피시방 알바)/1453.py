import sys

N = int(sys.stdin.readline())

listA = list(map(int, sys.stdin.readline().split()))
setA = set(listA)

print(len(listA) - len(setA))
