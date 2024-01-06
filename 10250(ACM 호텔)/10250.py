import sys

num = int(sys.stdin.readline())

for i in range(num) :
    H, W, person = map(int, sys.stdin.readline().split())
    if person % H == 0 :
        print(H*100+(person//H))
    else :
        print((person % H)*100 + ((person//H) + 1))
