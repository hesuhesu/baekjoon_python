import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())

listA = deque(list(range(1,N+1)))
result = []
while 1 :
    if len(listA) == 1 :
        result.append(listA[0])
        break

    for i in range(K-1) :
        listA.append(listA[0])
        listA.popleft()
    
    result.append(listA[0])
    listA.popleft()

result = list(map(str, result))

print("<{}>".format(', '.join(result)))
