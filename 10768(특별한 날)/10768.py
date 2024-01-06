import sys

M = int(sys.stdin.readline())
D = int(sys.stdin.readline())

if (M == 2) :
    if (D == 18):
        print("Special")
    elif (D > 18):
        print("After")
    else :
        print("Before")
elif (M > 2) :
    print("After")
else :
    print("Before")
