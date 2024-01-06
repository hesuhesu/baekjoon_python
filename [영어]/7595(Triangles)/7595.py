import sys

while 1 :
    n = int(sys.stdin.readline())

    if (n == 0) :
        break

    for i in range(n) :
        print("*" * (i+1))
