import sys

num = int(input())
listA = list(map(int, sys.stdin.readline().split()))
listA.sort()
print(listA[-1] * listA[0])
