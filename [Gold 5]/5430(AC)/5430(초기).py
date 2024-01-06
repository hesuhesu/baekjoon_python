import sys, re
from collections import deque

T = int(sys.stdin.readline())

for i in range(T) :
    stringA = sys.stdin.readline().strip()
    intA = int(sys.stdin.readline())
    listA = sys.stdin.readline().strip()
    listB = deque(re.findall(r'\d+', listA))
    result = 0
    for i in stringA :
        if i == 'R' :
            listB.reverse()
        elif i == 'D' :
            if len(listB) == 0 :
                result -= 1
                break
            else :
                listB.popleft()

    listB = list(listB)
    if result == -1 :
        print('error')
    else :
        print('[',end='')
        for i in range(len(listB)) :
            if i == len(listB)-1 :
                print(listB[i], end='')
            else :
                print(listB[i], end=',')
        print(']')
