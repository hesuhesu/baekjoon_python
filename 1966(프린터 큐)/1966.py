import sys

T = int(sys.stdin.readline())

for i in range(T):
    N,M = map(int, sys.stdin.readline().split())
    listA = list(map(int, sys.stdin.readline().split()))
    result = 0

    while 1 :
        if listA[0] == max(listA):
            result += 1
            del listA[0]
            M -= 1
            N -= 1
            if M == -1 :
                print(result)
                break
        else :
            listA.append(listA[0])
            del listA[0]
            M -= 1
            if M == -1 :
                M = N - 1