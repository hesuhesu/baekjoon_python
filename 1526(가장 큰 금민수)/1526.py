import sys

N = int(sys.stdin.readline())

for i in range(N,0,-1) :
    M = list(map(int, str(i)))
    result = 1
    for j in M :
        if ((j != 7) & (j != 4)) :
            result -= 1
            break
    if result == 1 :
        print(i)
        break
