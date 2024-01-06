import sys

N,K = map(int, sys.stdin.readline().split())

listA = []
for i in range(N) :
    A_i = int(sys.stdin.readline())
    if A_i > K :
        break
    else :
        listA.append(A_i)

listA.sort(reverse=True)
count = 0
for j in listA :
    if K % j == 0 :
        count += (K/j)
        break
    else :
        count += (K//j)
        K = K%j

print(int(count))
