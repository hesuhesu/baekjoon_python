import sys

while 1:
    M,W = map(int, sys.stdin.readline().split())
    if ((M==0)&(W==0)):
        break

    print(M+W)
