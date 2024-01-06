import sys

num = int(sys.stdin.readline())

for i in range(num) :
    floor = int(sys.stdin.readline())
    hosu = int(sys.stdin.readline())
    listA = list(map(int, range(1,hosu+1)))
    for j in range(floor) :
        for k in range(1,hosu) :
            listA[k] += listA[k-1]
    print(listA[-1])
