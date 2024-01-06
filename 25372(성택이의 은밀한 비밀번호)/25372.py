import sys

N = int(sys.stdin.readline())

for i in range(N) :
    stringA = sys.stdin.readline().strip()
    if (len(stringA) <= 9) & (len(stringA) >= 6) :
        print("yes")
    else :
        print("no")
