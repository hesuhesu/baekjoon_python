import sys

num1, num2 = map(int, sys.stdin.readline().split())

setA = set(map(int, sys.stdin.readline().split()))
setB = set(map(int, sys.stdin.readline().split()))

print(len(setA.difference(setB)) + len(setB.difference(setA)))
