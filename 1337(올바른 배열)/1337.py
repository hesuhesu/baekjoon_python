import sys

N = int(sys.stdin.readline())

listA = []
result = 5
for i in range(N):
    listA.append(int(sys.stdin.readline()))

for i in range(N):
    count1 = 4
    count2 = 4
    for j in range(N):
        if (listA[i] + 5 > listA[j]) & (listA[i] < listA[j]) :
            count1 -= 1
        elif (listA[i] - 5 < listA[j]) & (listA[i] > listA[j]) :
            count2 -= 1

    result = min(result, count1, count2)

print(result)
