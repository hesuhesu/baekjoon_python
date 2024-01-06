import sys

num = int(sys.stdin.readline())

for i in range(num) :
    listA = list(sys.stdin.readline().strip())
    print(listA[0]+listA[-1])
