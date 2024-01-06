import sys

while 1 :
    N1,N2 = map(int, sys.stdin.readline().split())

    if (N1 == 0) & (N2 == 0) :
        break

    if N1 > N2 :
        print('Yes')
    else :
        print('No')
