import sys

N, P = map(int, sys.stdin.readline().split())

listA = []
result = (N*N)%P
while 1 : 
    result = (N*result)%P

    if result in listA :
        print(len(listA) - listA.index(result))
        break
    listA.append(result)
