import sys

for i in range(3) :
    n = int(sys.stdin.readline())
    listB = []
    for j in range(n) :
        listB.append(int(sys.stdin.readline()))
    
    if sum(listB) == 0 :
        print('0')
    elif sum(listB) > 0 :
        print('+')
    else :
        print('-')
