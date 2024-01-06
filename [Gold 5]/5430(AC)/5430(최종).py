import sys, re
from collections import deque

T = int(sys.stdin.readline())

for i in range(T) :
    stringA = sys.stdin.readline().strip()
    intA = int(sys.stdin.readline())
    listA = sys.stdin.readline().strip()
    listB = deque(re.findall(r'\d+', listA))
    result = 0
    count = 0
    for i in stringA :
        if i == 'R' :
            count += 1
        elif i == 'D' :
            if len(listB) == 0 :
                result -= 1
                break
            else :
                if count % 2 == 0 :
                    listB.popleft()
                else :
                    listB.pop()

    listB = list(listB)
    if result == -1 :
        print('error')
    elif (result == 0) & (count % 2 == 0) :
        print('[' + ','.join(listB) + ']')
    elif (result == 0) & (count % 2 != 0) :
        listB.reverse()
        print('[' + ','.join(listB) + ']')
