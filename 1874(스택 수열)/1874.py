import sys
from collections import deque

N = int(sys.stdin.readline())
stack = deque()
result = deque()
checknum = 0
count = 1
for i in range(N) :
    M = int(sys.stdin.readline())

    while count <= M :
        stack.append(count)
        result.append('+')
        count += 1
    
    if stack[-1] == M :
        stack.pop()
        result.append('-')
    else :
        print('NO')
        checknum += 1
        break

if checknum == 0 :
    for _ in result :
        print(_)
