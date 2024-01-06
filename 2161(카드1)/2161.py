import sys
from collections import deque

N = int(sys.stdin.readline())
dq = deque(map(int, range(1,N+1)))

while 1 :
    print(dq.popleft(), end = ' ')
    if len(dq) == 0 :
        break
    dq.append(dq[0])
    dq.popleft()
