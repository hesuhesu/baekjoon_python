import sys

N, K = map(int, sys.stdin.readline().split())
listA = sorted(list(map(int, sys.stdin.readline().split())))

print(listA[K-1])
