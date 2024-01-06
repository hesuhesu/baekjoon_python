import sys

num1 = int(sys.stdin.readline())
list1 = set(map(int, sys.stdin.readline().split()))

num2 = int(sys.stdin.readline())
list2 = list(map(int, sys.stdin.readline().split()))

for i in list2 :
    if i in list1 :
        print(1, end=' ')
    else :
        print(0, end=' ')
