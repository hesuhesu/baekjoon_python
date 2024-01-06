import sys

N = int(sys.stdin.readline())

listA = list(map(int, sys.stdin.readline().split()))
listB = []
for i in range(1,N+1) :
    listB.insert(listA[i-1], i)
listB.reverse()

for i in listB :
    print(i, end = ' ')
