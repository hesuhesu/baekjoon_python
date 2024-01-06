import sys

N = int(sys.stdin.readline())
result = int(sys.stdin.readline())
count = 0
listA = []
if N == 1 :
    print(0)
else :
    for i in range(1,N) :
        listA.append(int(sys.stdin.readline()))
    listA.sort(reverse=True)

    while 1 :
        if result > listA[0] :
            break
        
        count += 1
        result += 1
        listA[0] -= 1
        listA.sort(reverse=True)

    print(count)
