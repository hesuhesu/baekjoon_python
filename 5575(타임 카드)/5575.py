import sys

listA = []
for i in range(3) :
    A = list(map(int, sys.stdin.readline().split()))
    A1_sum = A[0]*3600 + A[1]*60 + A[2]
    A2_sum = A[3]*3600 + A[4]*60 + A[5]
    listA.append(A2_sum - A1_sum)

listB = []
for i in range(3) :
    h = listA[i] // 3600
    w = (listA[i] % 3600) // 60
    s = (listA[i] % 3600) % 60
    listB.append([h,w,s])

for i in listB :
    for j in i :
        print(j, end = ' ')
    print("")
