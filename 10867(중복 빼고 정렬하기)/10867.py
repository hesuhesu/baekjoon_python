import sys

T = int(sys.stdin.readline())

listA = list(map(int, sys.stdin.readline().split()))
setA = sorted(set(listA))

for i in setA :
    print(i, end = " ")
