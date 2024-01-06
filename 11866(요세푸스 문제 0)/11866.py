import sys
from collections import deque

dq = deque()
N, K = map(int, sys.stdin.readline().split())

for i in range(1,N+1) :
    dq.append(i)

listA = []
while dq:
    for i in range(K-1):
        dq.append(dq.popleft())
    listA.append(dq.popleft())

print("<", end='')
print(', '.join(map(str, listA)), end='')
print(">")
