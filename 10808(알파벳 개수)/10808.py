import sys

stringA = list(map(str, sys.stdin.readline().strip()))
listA = [0]*26

for i in stringA :
    listA[ord(i)-97] += 1

for i in listA :
    print(i, end = " ")
