import sys

listA = sorted(list(map(int , sys.stdin.readline().split())))
print(listA[0] + listA[1] + min(listA[2], listA[0]+ listA[1]-1))