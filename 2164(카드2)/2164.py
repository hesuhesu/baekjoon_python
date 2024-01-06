import sys
from collections import deque

N = int(sys.stdin.readline())
dq = deque()

for i in range(1,N+1) :
    dq.append(i)

while 1 :
    if len(dq) == 1 :
        break

    dq.popleft()
    dq.append(dq[0])
    dq.popleft()

dq = list(dq)
print(dq[0])
