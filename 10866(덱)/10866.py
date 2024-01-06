import sys
from collections import deque

dq = deque()
N = int(sys.stdin.readline())

for i in range(N) :
    stringA = sys.stdin.readline().strip().split(' ')
    
    if stringA[0] == 'push_back' :
        dq.append(int(stringA[1]))
    elif stringA[0] == 'push_front' :
        dq.appendleft(int(stringA[1]))
    elif stringA[0] == 'pop_front' :
        if len(dq) == 0 :
            print(-1)
        else :
            print(dq.popleft())
    elif stringA[0] == 'pop_back' :
        if len(dq) == 0 :
            print(-1)
        else :
            print(dq.pop())
    elif stringA[0] == 'size' :
        print(len(dq))
    elif stringA[0] == 'empty' :
        if len(dq) == 0 :
            print(1)
        else :
            print(0)
    elif stringA[0] == 'front' :
        if len(dq) == 0 :
            print(-1)
        else :
            print(dq[0])
    elif stringA[0] == 'back' :
        if len(dq) == 0 :
            print(-1)
        else :
            print(dq[-1])
